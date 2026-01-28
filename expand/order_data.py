import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 设置随机种子以确保结果可重现
np.random.seed(42)

# ---------------------- 1. 用户表 ----------------------
users_data = {
    'user_id': range(1, 11),
    'user_name': [f'用户{i}' for i in range(1, 11)],
    'gender': np.random.choice(['男', '女'], size=10),
    'age': np.random.randint(18, 60, size=10),
    'city': np.random.choice(['北京', '上海', '广州', '深圳', '杭州', '成都'], size=10),
    'register_time': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 300)) for _ in range(10)]
}
users_df = pd.DataFrame(users_data)

# ---------------------- 2. 商品表 ----------------------
products_data = {
    'product_id': range(1, 16),
    'product_name': [f'商品{i}' for i in range(1, 16)],
    'category': np.random.choice(['电子产品', '服装鞋帽', '食品饮料', '家居用品', '美妆护肤'], size=15),
    'price': np.round(np.random.uniform(10.0, 2000.0, size=15), 2),
    'brand': np.random.choice(['品牌A', '品牌B', '品牌C', '品牌D', '品牌E'], size=15)
}
products_df = pd.DataFrame(products_data)

# ---------------------- 3. 订单表-上半年 ----------------------
order_h1_data = {
    'order_id': range(1, 51),
    'user_id': np.random.choice(range(1, 11), size=50),
    'product_id': np.random.choice(range(1, 16), size=50),
    'order_time': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 181)) for _ in range(50)],
    'quantity': np.random.randint(1, 5, size=50),
    'payment_method': np.random.choice(['支付宝', '微信支付', '银行卡'], size=50)
}
order_h1_df = pd.DataFrame(order_h1_data)

# 计算总金额
def calculate_total(row):
    product_price = products_df.loc[products_df['product_id'] == row['product_id'], 'price'].iloc[0]
    return np.round(row['quantity'] * product_price, 2)

order_h1_df['total_amount'] = order_h1_df.apply(calculate_total, axis=1)

# ---------------------- 4. 订单表-下半年 ----------------------
order_h2_data = {
    'order_id': range(51, 101),
    'user_id': np.random.choice(range(1, 11), size=50),
    'product_id': np.random.choice(range(1, 16), size=50),
    'order_time': [datetime(2023, 7, 1) + timedelta(days=np.random.randint(0, 184)) for _ in range(50)],
    'quantity': np.random.randint(1, 5, size=50),
    'payment_method': np.random.choice(['支付宝', '微信支付', '银行卡'], size=50)
}
order_h2_df = pd.DataFrame(order_h2_data)
order_h2_df['total_amount'] = order_h2_df.apply(calculate_total, axis=1)

# ---------------------- 5. 退货表 ----------------------
return_data = {
    'return_id': range(1, 21),
    'order_id': np.random.choice(range(1, 101), size=20),
    'return_time': [datetime(2023, 1, 3) + timedelta(days=np.random.randint(0, 362)) for _ in range(20)],
    'return_reason': np.random.choice(['商品质量问题', '尺码不合适', '买错商品', '不喜欢', '物流问题'], size=20),
    'refund_amount': np.round(np.random.uniform(10.0, 2000.0, size=20), 2),
    'return_status': np.random.choice(['已退款', '审核中', '已拒绝'], size=20)
}
return_df = pd.DataFrame(return_data)

# ---------------------- 保存到Excel文件 ----------------------
with pd.ExcelWriter('d:\Demo\dame.py\order_data.xlsx', engine='openpyxl') as writer:
    users_df.to_excel(writer, sheet_name='用户表', index=False)
    products_df.to_excel(writer, sheet_name='商品表', index=False)
    order_h1_df.to_excel(writer, sheet_name='订单表-上半年', index=False)
    order_h2_df.to_excel(writer, sheet_name='订单表-下半年', index=False)
    return_df.to_excel(writer, sheet_name='退货表', index=False)

print("数据已成功生成并保存到 order_data.xlsx 文件！")
print(f"\n表结构信息：")
print(f"1. 用户表: {len(users_df)} 条记录")
print(f"2. 商品表: {len(products_df)} 条记录")
print(f"3. 订单表-上半年: {len(order_h1_df)} 条记录")
print(f"4. 订单表-下半年: {len(order_h2_df)} 条记录")
print(f"5. 退货表: {len(return_df)} 条记录")

# ---------------------- 提供pandas合并操作示例 ----------------------
print("\n\nPandas合并操作示例:")
print("=" * 50)

# 示例1: 合并订单表上半年和用户表
df_merge1 = pd.merge(order_h1_df, users_df, on='user_id', how='left')
print(f"示例1: 订单表上半年 + 用户表 (左连接)\n{df_merge1[['order_id', 'user_name', 'product_id', 'total_amount']].head()}")

# 示例2: 合并订单表上半年和商品表
df_merge2 = pd.merge(order_h1_df, products_df, on='product_id', how='left')
print(f"\n示例2: 订单表上半年 + 商品表 (左连接)\n{df_merge2[['order_id', 'product_name', 'category', 'price', 'total_amount']].head()}")

# 示例3: 合并两个订单表
df_merge3 = pd.concat([order_h1_df, order_h2_df], ignore_index=True)
print(f"\n示例3: 订单表上半年 + 订单表下半年 (纵向合并)\n总记录数: {len(df_merge3)}")

# 示例4: 合并订单表和退货表
df_merge4 = pd.merge(df_merge3, return_df, on='order_id', how='left')
print(f"\n示例4: 合并后的订单表 + 退货表 (左连接)\n{df_merge4[['order_id', 'user_id', 'product_id', 'total_amount', 'return_status']].head()}")

# 示例5: 多表联合查询
df_full = pd.merge(df_merge2, users_df, on='user_id', how='left')
df_full = pd.merge(df_full, return_df, on='order_id', how='left')
print(f"\n示例5: 完整订单信息表 (订单+商品+用户+退货)\n{df_full[['order_id', 'user_name', 'product_name', 'category', 'total_amount', 'return_status']].head()}")
