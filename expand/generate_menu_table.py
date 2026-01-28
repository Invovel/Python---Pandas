import pandas as pd
import numpy as np
import os

# 设置随机种子以确保结果可重现
np.random.seed(42)

# 菜品数据
dishes = ['宫保鸡丁', '麻婆豆腐', '鱼香肉丝', '回锅肉', '水煮鱼', '糖醋里脊', '红烧肉', '京酱肉丝']
colors = ['红色', '棕色', '黄色', '绿色', '白色', '黑色']

# 生成随机数据
menu_data = {
    '菜品': np.random.choice(dishes, size=100),
    '颜色': np.random.choice(colors, size=100),
    '价格': np.round(np.random.uniform(20.0, 80.0, size=100), 2),
    '数量': np.random.randint(1, 10, size=100)
}

# 创建DataFrame
menu_df = pd.DataFrame(menu_data)

# ---------------------- 计算分组统计信息 ----------------------
# 按菜品分组统计
dish_group = menu_df.groupby('菜品').agg({
    '价格': ['mean', 'sum', 'max', 'min'],
    '数量': ['sum', 'count', 'mean']
}).round(2)

# 重命名列
dish_group.columns = ['平均价格', '总销售额', '最高价格', '最低价格', '总销量', '销售次数', '平均销量']

# 按颜色分组统计
color_group = menu_df.groupby('颜色').agg({
    '价格': ['mean', 'sum'],
    '数量': ['sum', 'count']
}).round(2)

# 重命名列
color_group.columns = ['平均价格', '总销售额', '总销量', '销售次数']

# 按菜品和颜色双重分组
dish_color_group = menu_df.groupby(['菜品', '颜色']).agg({
    '价格': ['mean', 'sum'],
    '数量': ['sum']
}).round(2)

# 重命名列
dish_color_group.columns = ['平均价格', '总销售额', '总销量']

# ---------------------- 保存到Excel文件 ----------------------
# 确保目录存在
try:
    # 确保安装了openpyxl
    import openpyxl
    
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 保存到上级目录
    output_file = os.path.join(current_dir, '..', 'menu_table.xlsx')
    output_file = os.path.normpath(output_file)  # 规范化路径
    
    # 使用ExcelWriter保存
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # 原始数据
        menu_df.to_excel(writer, sheet_name='原始数据', index=False)
        
        # 按菜品分组统计
        dish_group.to_excel(writer, sheet_name='按菜品分组')
        
        # 按颜色分组统计
        color_group.to_excel(writer, sheet_name='按颜色分组')
        
        # 按菜品和颜色双重分组
        dish_color_group.to_excel(writer, sheet_name='按菜品-颜色分组')

    print(f"数据已成功生成并保存到 {output_file} 文件！")
    print(f"\n文件包含以下工作表：")
    print(f"1. 原始数据: {len(menu_df)} 条菜品销售记录")
    print(f"2. 按菜品分组: 统计各菜品的价格和销量信息")
    print(f"3. 按颜色分组: 统计各颜色菜品的价格和销量信息")
    print(f"4. 按菜品-颜色分组: 双重分组统计详细信息")
    
except ImportError:
    print("错误：未安装 openpyxl 库！请先运行：pip install openpyxl")
except Exception as e:
    print(f"生成文件时出现错误: {e}")
    print("当前工作目录:", os.getcwd())
