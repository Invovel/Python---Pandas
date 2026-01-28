import json
import os
import pandas as pd
from collections import Counter
import zipfile
import re
from datetime import datetime

# 设置需要记录的药品名称
KEYWORDS = ["Metformin", "Propranolol", "Captopril", "Atorvastatin", 
            "Sertraline", "Valproate", "Prednisone", "Amiodarone"]

def is_valid_drug_name(drug_name):
    """验证药物名称是否有效"""
    if not drug_name:
        return False
        
    drug_name = drug_name.lower().strip()
    # 检查是否包含任何关键词
    return any(keyword.lower() in drug_name for keyword in KEYWORDS)

def convert_age_to_years(age, unit):
    """将年龄统一转换为年"""
    if not age or not unit:
        return None
    try:
        age = float(age)
        unit = unit.lower()
        if unit == 'year' or unit == 'years':
            return age
        elif unit == 'month' or unit == 'months':
            return age / 12
        elif unit == 'day' or unit == 'days':
            return age / 365
        else:
            return None
    except:
        return None

def standardize_drug_name(name):
    """标准化药物名称"""
    if not name:
        return ""
    # 转换为小写并去除多余空格
    name = name.lower().strip()
    # 标准化常见剂型
    name = re.sub(r'\s+tablet\b', '', name)
    name = re.sub(r'\s+capsule\b', '', name)
    name = re.sub(r'\s+injection\b', '', name)
    return name

def standardize_route(route):
    """标准化给药途径"""
    if not route:
        return ""
    route = route.lower()
    # 标准化常见给药途径
    route_mapping = {
        'oral': 'oral',
        'po': 'oral',
        'intravenous': 'iv',
        'iv': 'iv',
        'subcutaneous': 'sc',
        'sc': 'sc',
        'intramuscular': 'im',
        'im': 'im',
        'topical': 'topical',
        'inhalation': 'inhalation',
        'rectal': 'rectal'
    }
    return route_mapping.get(route, route)

def validate_date(date_str):
    """验证日期格式"""
    if not date_str:
        return None
    try:
        # 尝试解析各种可能的日期格式
        for fmt in ['%Y-%m-%d', '%Y/%m/%d', '%d/%m/%Y', '%d-%m-%Y']:
            try:
                return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')
            except:
                continue
        return None
    except:
        return None

def extract_adverse_reaction_info(data):
    """Extract drug adverse reaction information based on JSON structure"""
    results = []
    
    if not isinstance(data, dict):
        return results
        
    # Extract patient information
    patient_info = data.get('patient', {})
    safety_report_id = data.get('safetyreportid', '')
    
    # 验证必填字段
    if not safety_report_id:
        return results
        
    # Extract patient basic information
    age = convert_age_to_years(
        patient_info.get('patientonsetage', ''),
        patient_info.get('patientonsetageunit', '')
    )
    
    patient_data = {
        'safety_report_id': safety_report_id,
        'age': age,
        'weight': patient_info.get('patientweight', ''),
        'sex': patient_info.get('patientsex', '')
    }
    
    # Extract drug information
    drugs = patient_info.get('drug', [])
    reactions = patient_info.get('reaction', [])
    
    # 验证至少有一个药物和一个不良反应
    if not drugs or not reactions:
        return results
        
    for drug in drugs:
        medicinal_product = drug.get('medicinalproduct', '')
        
        # 验证药物名称是否有效
        if not is_valid_drug_name(medicinal_product):
            continue
            
        drug_info = {
            'drugcharacterization': drug.get('drugcharacterization', ''),
            'medicinalproduct': standardize_drug_name(medicinal_product),
            'drugdosageform': drug.get('drugdosageform', ''),
            'drugdosagetext': drug.get('drugdosagetext', ''),
            'drugadministrationroute': standardize_route(drug.get('drugadministrationroute', '')),
            'drugindication': drug.get('drugindication', ''),
            'drugstartdate': validate_date(drug.get('drugstartdate', '')),
            'drugenddate': validate_date(drug.get('drugenddate', '')),
            'activesubstance': drug.get('activesubstance', {}).get('activesubstancename', '')
        }
        
        # Extract specific fields from openfda
        openfda = drug.get('openfda', {})
        if openfda:
            drug_info.update({
                'product_type': openfda.get('product_type', []),
                'route': openfda.get('route', []),
                'substance_name': openfda.get('substance_name', []),
                'rxcui': openfda.get('rxcui', []),
                'unii': openfda.get('unii', [])
            })
        
        # Extract adverse reactions
        for reaction in reactions:
            reaction_info = {
                'reactionmeddraversionpt': reaction.get('reactionmeddraversionpt', ''),
                'reactionmeddrapt': reaction.get('reactionmeddrapt', '')
            }
            
            # Combine all information
            result = {
                **patient_data,
                **drug_info,
                **reaction_info
            }
            results.append(result)
    
    return results

def process_json_file(file_path):
    """Process a single JSON file and return extracted data"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return extract_adverse_reaction_info(data)
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return []

def process_zip_file(zip_path):
    """Process a ZIP file containing JSON files"""
    results = []
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for file_name in zip_ref.namelist():
                if file_name.endswith('.json'):
                    with zip_ref.open(file_name) as f:
                        data = json.load(f)
                        results.extend(extract_adverse_reaction_info(data))
    except Exception as e:
        print(f"Error processing ZIP {zip_path}: {str(e)}")
    return results

def save_drug_data(data, output_dir, year, quarter):
    """Save data for each drug in separate files"""
    if not data:
        return
        
    # Group data by drug
    drug_data = {}
    for record in data:
        drug_name = record['medicinalproduct']
        for keyword in KEYWORDS:
            if keyword.lower() in drug_name.lower():
                if keyword not in drug_data:
                    drug_data[keyword] = []
                drug_data[keyword].append(record)
    
    # Save data for each drug
    for drug, records in drug_data.items():
        output_file = os.path.join(output_dir, f"{drug}_{year}Q{quarter}_data.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(records)} records for {drug} in {year}Q{quarter}")

def create_analysis_excel(data, output_file, year, quarter):
    """Create Excel files with analysis of adverse reactions"""
    if not data:
        print("No data to process")
        return
        
    try:
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Remove duplicates
        df = df.drop_duplicates()
        
        # Create Excel writer
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            # Write raw data
            df.to_excel(writer, sheet_name='Raw Data', index=False)
            
            # Create summary statistics
            # Count adverse reactions
            reaction_counter = Counter()
            for reaction in df['reactionmeddrapt']:
                reaction_counter[reaction] += 1
            
            # Create reaction summary
            reaction_summary = pd.DataFrame({
                'Reaction': list(reaction_counter.keys()),
                'Count': list(reaction_counter.values())
            }).sort_values('Count', ascending=False)
            
            # Create drug-reaction summary
            drug_reaction_summary = []
            for _, row in df.iterrows():
                drug_reaction_summary.append({
                    'Drug': row['medicinalproduct'],
                    'Reaction': row['reactionmeddrapt'],
                    'Route': row['drugadministrationroute'],
                    'Characterization': row['drugcharacterization'],
                    'Age': row['age'],
                    'Sex': row['sex']
                })
            
            drug_reaction_df = pd.DataFrame(drug_reaction_summary)
            
            # Write summary sheets
            reaction_summary.to_excel(writer, sheet_name='Reaction Summary', index=False)
            drug_reaction_df.to_excel(writer, sheet_name='Drug-Reaction Summary', index=False)
            
            # Format sheets
            for sheet_name in writer.sheets:
                worksheet = writer.sheets[sheet_name]
                # Auto-adjust column widths
                for column in worksheet.columns:
                    max_length = 0
                    column = [cell for cell in column]
                    for cell in column:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    adjusted_width = (max_length + 2)
                    worksheet.column_dimensions[column[0].column_letter].width = adjusted_width
    except Exception as e:
        print(f"Error creating Excel file: {str(e)}")
        raise

def process_quarter(year, quarter, base_dir):
    """Process a single quarter's data"""
    input_dir = os.path.join(base_dir, str(year), f"q{quarter}")
    output_dir = "E:\\FAERS Data\\data"  # 固定输出目录

    
    if not os.path.exists(input_dir):
        print(f"Directory not found: {input_dir}")
        return False
        
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Process all files in the input directory
        all_data = []
        for file_name in os.listdir(input_dir):
            try:
                if file_name.endswith('.json'):
                    file_path = os.path.join(input_dir, file_name)
                    data = process_json_file(file_path)
                    all_data.extend(data)
                    print(f"Processed {file_name}")
                elif file_name.endswith('.zip'):
                    file_path = os.path.join(input_dir, file_name)
                    data = process_zip_file(file_path)
                    all_data.extend(data)
                    print(f"Processed ZIP {file_name}")
            except Exception as e:
                print(f"Error processing {file_name}: {str(e)}")
                continue
        
        # Save data for each drug
        save_drug_data(all_data, output_dir, year, quarter)
        
        # Create analysis Excel
        if all_data:
            output_file = os.path.join(output_dir, f"adverse_reaction_analysis_{year}Q{quarter}.xlsx")
            create_analysis_excel(all_data, output_file, year, quarter)
            print(f"Created analysis file: {output_file}")
            return True
        else:
            print("No data was processed successfully")
            return False
            
    except Exception as e:
        print(f"Error processing quarter {year} Q{quarter}: {str(e)}")
        return False

def main():
    # Define base directory
    base_dir = "E:\\FAERS Data"

    # Process years from 2019 to 2024
    for year in range(2019, 2025):
        print(f"\nProcessing year {year}...")
        
        # Process each quarter
        for quarter in range(1, 5):
            # Skip Q4 for 2024 if it doesn't exist
            if year == 2024 and quarter == 4:
                q4_dir = os.path.join(base_dir, str(year), "q4")
                if not os.path.exists(q4_dir):
                    print(f"Skipping {year} Q4 - directory not found")
                    continue
            
            print(f"\nProcessing {year} Q{quarter}...")
            success = process_quarter(year, quarter, base_dir)
            
            if success:
                print(f"Successfully processed {year} Q{quarter}")
            else:
                print(f"Failed to process {year} Q{quarter}")

if __name__ == "__main__":
    main()
