# name = "Alice"
# age = 30.5
# # 普通输出
# print(f"{name} is {age:05.1f} years old.")
# # 或者保留 debug 风格（会打印变量名=值）
# print(f"{name=} is {age=:05.1f} years old.")

# for _ in "hello":
#     print("Hi" + _) 
#     print(f"Hi{_}")

# print( f"{4.3e2}", end='\t')#

# import pandas as pd
# import numpy as np

# from pandas import DataFrame, Series

# List_1 = [1, 2, 'name']
# s1 = pd.Series(data = List_1)# In[]: pd.Series(List_1)
# print(s1)# Out[]:

import pandas as pd
import numpy as np

from pandas import DataFrame, Series

#构造DataFrame
#3x4二维数组
# data = np.random.randint(0, 100, size = (3, 4))# In[]: data
# index = ['Tom', 'Jack', 'Steve']# In[]: index -> 行
# columnns = ['Chinese', 'Math', 'Physical', 'Chemistry']# In[]: columns -> 列
# pd.DataFrame(data = data, index = index, columns = columnns)# In[]: pd.DataFrame(data, index, columns)
# # Out[]: 3行4列的表格数据
# print(pd.DataFrame(data = data, index = index, columns = columnns))

# from IPython.display import display
# names = ['Tom', 'Jack', 'Steve', 'Ricky', 'Mary']# In[]: names
# chinese_scores =  np.random.randint(0, 100, size = 5)# In[]: chinese_scores
# math_scores =  np.random.randint(0, 100, size = 5)# In[]: math_scores
# display(names, chinese_scores, math_scores)# Out[]:
# dict_data = {
#     'Name': names,
#     'Chinese': chinese_scores,
#     'Math': math_scores
#     }# In[]: dict_data
# pd.DataFrame(dict_data)# In[]: pd.DataFrame(dict_data)
# # Out[]: 5行3列的表格数据


#1) From dict of Series or list: 由Series构造的字典或一个字典构造
# name = pd.Series(data = ['Tom', 'Jack', 'Steve'], index = list('ABC'))# In[]: name
# scores = pd.Series(data = np.random.randint(0, 100, size = 3), index = list('ABC'))# In[]: scores
# print(pd.DataFrame(data = {
#     'Name': name,
#     'Scores': scores
# }))# In[]: dict of Series; {} -> dict 

#2) From dict of ndarrays / lists: 由ndarray或list构造的字典
# data = {
#     'Name': ['Tom', 'Jack', 'Steve'],
#     'Scores': np.random.randint(0, 100, size = 3)
#     }# In[]: data dict of ndarrays / lists
# pd.DataFrame(data = data, index = 3)# In[]: pd.DataFrame(data)
# print(pd.DataFrame(data = data, index = 3))

#3) From a list of dicts: 由字典列表构造
# data_1 = {
#     'Name': ['Tom', 'Jack', 'Steve'],
#     'Chinese_Scores': np.random.randint(0, 100, size = 3)
#     }# In[]: data dict of ndarrays / lists
# data_2 = {
#     'Name': ['Tom', 'Jack', 'Steve'],
#     'Math_Scores': np.random.randint(0, 100, size = 3)
#     }# In[]: data dict of ndarrays / lists
# pd.DataFrame([data_1, data_2])# In[]: pd.DataFrame( [dict1, dict2] ) 列索引取并集，缺失值补NaN
# # Out[]: 2行3列的表格数据
# print(pd.DataFrame([data_1, data_2]))

# df = pd.DataFrame(data = np.random.randint(0, 10, size = (3, 4)), 
#              index = list('ABC'), 
#              columns = list('WXYZ')) + 1# In[]: DataFrame + 1: 每个元素都加1
# # Out[]: 每个元素都加1
# print(df)# In[]: df
# arry_1 = np.array([
#     [1, 2, 3, 4]
#     ])# In[]: arry_1 1x4 ndarray
# print(df + arry_1)# In[]: df + arry_1 按位置对应元素运算
# # Out[]: 每行都加上arry_1对应元素的值
# arry_2 = arr1.reshape(2, 2).copy()# In[]: arry_2 2x2 ndarray
# print(df + arry_2)# In[]: df + arry_2 按广播规则运算
# # Out[]: 报错，无法广播运算


# # 生成3x3随机整数数组（-10到9）
# arr = np.random.randint(-10, 10, size=(3, 3))
# # 转成DataFrame
# df = pd.DataFrame(data=arr)

# print("原始3x3表格：")
# print(df)
# print("\n所有元素取绝对值后的表格：")
# print(np.abs(df))


# pd.MultiIndex()# 多层索引对象，用于存储轴标签（行标签、列标签）
Level1 = ['第二期', '第二期']
Level2 = ['A', 'B', 'C']
columns = pd.MultiIndex.from_product([Level1, Level2], names=['期数', '产品'])# 使用product()方法创建多层索引
# index = ['Lucy', 'Lily', 'Rose']
index = pd.Index(['Lucy', 'Lily', 'Rose'], name='姓名')
data = np.random.randint(0, 100, size=(3, 6))
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)
