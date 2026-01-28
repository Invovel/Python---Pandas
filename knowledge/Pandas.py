'''Series'''#dict-like 1D array
Values = [1, 2, 3, 4]#数据 ndarray-like
Index = ['a', 'b', 'c', 'd']#索引 Index-like
# Series一堆数组（values）+ 一堆索引（index） ≠ 字典（key-value）【区别在于：Series的索引可以重复，而字典的key不可以重复】
#构造Series
import pandas as pd
import numpy as np# pd.Series()  # pd.Series(数据, 索引) pd是pandas的别名（自主命名）

from pandas import Series, DataFrame

'''
pd.Series(data = None, index = None, dtype=None, name=None, copy=False, fastpath=False)
'''
arr1 = np.random.randint(0, 10, size=5)# In[]: arr1
print(arr1)# Out[]: array([0, 1, 2, 3, 4])
s1 = pd.Series(data = arr1)# In[]: pd.Series(arr1)
print(s1)# Out[]:

#index指定的显示索引，无定义，则为隐式索引（数组索引）0,1,2,3,4...
s2 = pd.Series(data = arr1, index = ['A', 'B', 'C', 'D', 'E'])# In[]: pd.Series(Values, Index)
print(s2)# Out[]:

L1=[1, 2, 3, 4]# In[]: L1 type(L1) == list
s3 = pd.Series(data = L1, index = list('ABCD'))# In[]: pd.Series(L1) index 与 data 长度必须相同
print(s3)# Out[]:

arr1[0]=100# In[]: arr1
print(s1)# Out[]: Series数据不会随着arr1的变化而变化，Series会复制一份数据
print(arr1)# Out[]:

user_info={
    'name': 'zhangsan', 
    'age': 18, 
    'gender': 'male'
    }# In[]: user_info type(user_info) == dict

# In[]: pd.Series(user_info, index = ['A', 'B', 'C']) index指定的索引不存在于字典中，则对应数据为NaN
print(pd.Series(data = user_info, index = ['A', 'B', 'C']))# Out[]:
#NAN表示缺失值 Not a Number 空值

print(pd.Series(data = user_info))# In[]: pd.Series(user_info) 字典的key作为Series的索引，value作为Series的数据
# Out[]:

print(pd.Series(data = user_info, index = ['name', 'age', 'A']))# In[]: pd.Series(user_info, index = ['name', 'age'])

'''From scalar value'''#单值构造Series 必须指定index
s4 = pd.Series(data = 5, index = ['A', 'B', 'C', 'D'])# In[]: pd.Series(5, index = ['A', 'B', 'C', 'D'])
print(s4)# Out[]:

'''Series属性'''
'''
name # Series名称
index # Series索引
values # Series数据 ndarray-like
dtype # Series数据类型
size # Series数据个数
shape # Series数据形状

pd.Series(data = None, index = None, dtype=None, name=None, copy=False, fastpath=False)
'''
#访问数据
s4.A == s4['A']# In[]: s4.A 通过属性名访问数据: name形式s4.index 和 字典dict形式 s4['Index']
# df.shape#数据形状 (行数, 列数)
# df.size#数据个数 行数*列数

#Series数学运算
# 索引对齐原则：对不齐补空值NaN，用add、sub、mul、div等方法，指定fill_value参数补齐空值

#1) 非pandas对象参与运算，广播机制
s = pd.Series([1, 2, 3], index = ['A', 'B', 'C'])# In[]: s
s + 1# Out[]: 每个元素都加1
arr1 + s# In[]: arr1 + s 按位置对应元素运算
# Out[]: array([101,  3,  5, nan, nan]) arr1长度大于s，超出部分补NaN

#2) NumPy数组参与运算，按位置对应元素运算
np.power(pd.array[1, 2, 3, 4], 2)# In[]: np.power(s, 2)
# Out[]: 每个元素都平方

#3) Series对象参与运算，按索引对应元素运算
s_1 = pd.Series([1, 2, 3], index = ['A', 'B', 'C'])# In[]: s1
s_2 = pd.Series([4, 5, 6], index = ['B', 'C', 'D'])# In[]: s2
s_1 + s_2# In[]: s1 + s2 按索引(按顺序)对应元素运算
# Out[]: 索引不对齐的部分补NaN
s_1.add(s_2, fill_value=0)# In[]: s1.add(s2, fill_value=0) 指定fill_value参数补齐空值
s_1.subtract(s_2, fill_value=0)# In[]: s1.subtract(s2, fill_value=0) subtraction减法
s_1.multiply(s_2, fill_value=1)# In[]: s1.multiply(s2, fill_value=1) multiplication乘法
s_1.divide(s_2, fill_value=1)# In[]: s1.divide(s2, fill_value=1) division除法



'''DataFrame'''#二维表格数据结构
#构造DataFrame：inndex（行索引）相同、columns（列索引）不同
'''pd.DataFrame(data = None, index = None, columns = None, dtype=None, copy=False)
data: 2D ndarray, list, dict, Series, DataFrame
index: 行索引 Index-like
columns: 列索引 Index-like
dtype: 数据类型
copy: 复制数据
'''

import pandas as pd
import numpy as np

from pandas import DataFrame, Series

List_1 = [1, 2, 'name']
s1 = pd.Series(data = List_1)# In[]: pd.Series(List_1)
print(s1)# Out[]:
#Series 和ndarray的区别在于：Series有索引index，而ndarray没有索引，但都会强制转换为ndarray存储

#构造DataFrame

#3x4二维数组
data = np.random.randint(0, 100, size=(3, 4))# In[]: data
index = ['Tom', 'Jack', 'Steve']# In[]: index -> 行
columns = ['Chinese', 'Math', 'Physical', 'Chemistry']# In[]: columns -> 列
pd.DataFrame(data = data, index = index, columns = columns)# In[]: pd.DataFrame(data, index, columns)
# Out[]: 3行4列的表格数据


#1) From dict of Series or list: 由Series构造的字典或一个字典构造
name = pd.Series(data = ['Tom', 'Jack', 'Steve'], index = list('ABC'))# In[]: name
scores = pd.Series(data = np.random.randint(0, 100, size=3), index = list('ABC'))# In[]: scores
pd.DataFrame(data = {
    'Name': name,
    'Scores': scores
})# In[]: dict of Series; {} -> dict 


#2) From dict of ndarrays / lists: 由ndarray或list构造的字典
data = {
    'Name': ['Tom', 'Jack', 'Steve'],
    'Scores': np.random.randint(0, 100, size=3)
    }# In[]: data dict of ndarrays / lists
pd.DataFrame(data = data, index = 3)# In[]: pd.DataFrame(data) index = [] -> 指定行索引 


#3) From a list of dicts: 由字典列表构造
data_1={
    'Name': ['Tom', 'Jack', 'Steve'],
    'Chinese_Scores': np.random.randint(0, 100, size=3)
    }# In[]: data dict of ndarrays / lists
data_2={
    'Name': ['Tom', 'Jack', 'Steve'],
    'Math_Scores': np.random.randint(0, 100, size=3)
    }# In[]: data dict of ndarrays / lists
pd.DataFrame([data_1, data_2])# In[]: pd.DataFrame( [dict1, dict2] -> []) 列索引取并集，缺失值补NaN
# Out[]: 2行3列的表格数据


#4) DataFrame.from_dict(): 由字典构造DataFrame 可在不同列之间出现不同的类型
from IPython.display import display
names = ['Tom', 'Jack', 'Steve', 'Ricky', 'Mary']# In[]: names
chinese_scores =  np.random.randint(0, 100, size=5)# In[]: chinese_scores
math_scores =  np.random.randint(0, 100, size=5)# In[]: math_scores
display(names, chinese_scores, math_scores)# Out[]: display显示多个变量的值,不改变变量本身
dict_data = {
    'Name': names,
    'Chinese': chinese_scores,
    'Math': math_scores
    }# In[]: dict_data
pd.DataFrame(dict_data)# In[]: pd.DataFrame(dict_data)
# Out[]: 5行3列的表格数据


#5) DataFrame.from_records(): 由记录数组构造DataFrame
data = np.random.randint(0, 100, size=(5, 3))# In[]: data 5行3列的二维数组
records = np.core.records.fromarrays(data.T, names = 'Chinese, Math, Physical')# In[]: records 记录数组
pd.DataFrame.from_records(records)# In[]: pd.DataFrame.from_records(records)


'''DataFrame属性'''
#1) dtypes: 每"列"(多个)数据类型
#2) values: DataFrame数据 ndarray-like
#3) index: 行索引 Index-like
#4) columns: 列索引 Index-like
#5) shape: 数据形状 (行数, 列数)

'''nndarry VS DataFrame'''
# ndarray: 只能存储单一数据类型的数据
# DataFrame: 每列可以存储不同数据类型的数据
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ])# In[]: data ndarray 3x3

'''DataFrame数学运算'''
#1) 非pandas对象参与运算，广播机制
df = pd.DataFrame(data = np.random.randint(0, 10, size=(3, 4)), 
             index = list('ABC'), 
             columns = list('WXYZ')) + 1# In[]: DataFrame + 1: 每个元素都加1
# Out[]: 每个元素都加1
arry_1 = np.array([
    [1, 2, 3, 4]
    ])# In[]: arry_1 1x4 ndarray
df + arry_1# In[]: df + arry_1 按位置对应元素运算
# Out[]: 每行都加上arry_1对应元素的值


#2) Series对象参与运算，按索引对应元素运算
s = pd.Series([1, 2, 3, 4], index = list('WXYZ'))# In[]: series 1D
df + s# In[]: df + s 按列索引对应元素运算
# Out[]: 每列都加上s对应元素的值
# 无法对应输出的索引，补NaN


#3) DataFrame对象参与运算，按行列索引对应元素运算
#· 行列索引都对齐，按位置对应元素运算 -> row \ column alignment
#· 行列索引不对齐，补NaN -> add、sub、mul、div等方法，指定fill_value参数补齐空值; 不支持DataFrame 和 Series 间运算
# df1.add(df2, fill_value=0)


#4) NumPy functions
#python operator => pandas method
# + => add(list, axis = 0/1(0 / 1 =>'index' or 'columns'), level=None, fill_value=value)
# - => sub(), subtract()
# * => mul(), multiply()
# # ** => pow()
# / => div(), divide(), truediv()
# // => floordiv()
# % => mod()

# DataFrame and Series:列表对齐原则
# NaN参与运算结果仍为缺失值NaN

# 生成3x3随机整数数组（-10到9）
arr = np.random.randint(-10, 10, size=(3, 3))
# 转成DataFrame
df = pd.DataFrame(data = arr)

print("原始3x3表格：")
print(df)
print("\n所有元素取绝对值后的表格：")
print(np.abs(df))# abs(df)=abs(arr)


#5) 转置运算
# df.T



'''
Pandas 访问
'''
# ndarray[ndiml_index, ndim2_index ...]
# index:索引、 索引列表、 Bool列表、 切片、 条件表达式
arr[0]=10
arr2 = np.random.randint(0, 10, size=(5, 6))
#索引、 索引列表
arr2[[0, 1]]#访问前两行
arr2[:, [0, 1]]#:切片 访问前两列
arr2[0, 1]=100#赋值


'''Basics 标准访问形式'''
#显示访问：df.loc[行索引, 列索引]，在pandas中，可以使用标签的形式访问数据 -> 标签Labels
# Series -> s.loc[indexer]
# DataFrame -> df.loc[row_indexer, columns_indexer]

'''Labels：标签名，标签名列表，Bool列表(没有标签的，有标签的)，切片'''
# s.loc[labels]
# df.loc[row_labels, column_labels]

#BOOL
s = pd.Series(data = np.array(True, False, True), index = list('ABC'))# In[]: s 有Labels
array = np.array([True, False, True])# In[]: array 无Labels

#切片 
s[0:2] / s['A':'B']#前者为位置切片->左闭右开，后者为标签切片->闭合区间
s[:2]#左闭右开
s[0, list('ABCDEF')]
s.loc[:,['A', 'B']]#获取第1、2列的数据
s.loc[[1, 2], ['B', 'C']]#获取第2、3行，第2、3列的数据
bool_list = pd.Series(data = np.array[True, True, False, False], index = list[0, 4, 3, 1, 2])# In[]: bool_list获取标签为0、4、3、1、2的元素; np.array可省略


#隐式访问：df.iloc[行索引, 列索引]，在pandas中，可以使用位置的形式（index等）访问数据 -> 索引Indexer
# Series -> s.iloc[indexer]
# DataFrame -> df.iloc[row_indexer, columns_indexer]
s.iloc[index]
df.iloc[row_indexer, column_indexer]
# index: index, index列表, Bool列表, 切片, 条件表达式


'''多层索引'''

'''间接访问'''
df.loc[0].loc['A']=df.loc[0, 'A']#嵌套访问 -> 先按行索引(DataFrame -> Series)，再按列索引(Series -> 单个值):间接访问:拆分访问
#隐患：索引越界，报错; 多重副本

df.loc[0, 'A']#直接访问 -> 先按行索引(dict-like)，再按列索引(Str -> 单个值):直接访问
df[['A', 'B']]=df.loc[:, ['A', 'B']]# 访问多列数据 -> dict-like column selection => dict_indexer
# []: 标签访问多列数据、剪切行 -> list-like column selection => list_indexer

'''where() and mask()'''
# where()# 条件(condition)为True时，返回原数据；条件为False时，返回其他值(other)
# mask()# 条件(condition)为True时，返回其他值；条件为False时，返回原数据
df = pd.DataFrame(data = np.random.randint(0, 100, size=(5, 4)), columns = list('ABCD'))
#Bool:condition:df > 50 -> True False
df = df.where(cond=df > 60, other="不及格")# 大于60的保留，小于等于60的替换为"不及格"
df = df.mask(cond=df < 60, other="及格")# 小于60的替换为"及格"，大于等于60的保留

# 高级
df = df.where(cond=df > 60, other = pd.Series(data = [100, 200], index = list('AB'), anext=1))# 大于60的保留，小于等于60的替换为100（A列）、200（B列）,anext => columns方向


'''The query() method'''
# query()# 条件(condition)为True时，返回原数据；条件为False时，返回空DataFrame
df = pd.DataFrame(data = np.random.randint(0, 100, size=(5, 4)), columns = list('ABCD'))
df.query(expr="A > 60 and B > 60", inplace=True)# 同时满足A、B大于60的行
df.query("A > 60 or B > 60")# 满足A、B大于60的行
df.query("A > 60 and B > 60 and C > 60")# 同时满足A、B、C大于60的行
df.query("A > 60 or B > 60 or C > 60")# 满足A、B、C大于60的行
df.query("B == 60")# 满足B等于60的行


'''The filter() method'''
filter(items = '选择的列名列表', axis = 0/1, regex = '正则表达式,模糊匹配', )
df.columns = ['AA', 'BB', 'CC', 'DD']
df.filter(items = ['AA', 'BB'], axis = 1)# 筛选列名包含'AA'、'BB'的列
df.filter(like='B', axis = 1)# 筛选列名包含'B'的列
df.filter(regex = '^A', axis = 1)# 筛选列名以'A'开头的列
# 'B'='.*B.*' # 筛选列名包含'B'的列
# '^A'='A.*' # 筛选列名以'A'开头的列
# '^A$'='A' # 筛选列名只有'A'的列
# '^.$'='.' # 筛选列名只有一个字符的列
# '^[A-Z]$'=[A-Z] # 筛选列名只有一个大写字母的列
# '^[a-z]$'=[a-z] # 筛选列名只有一个小写字母的列
# '^[0-9]$'=[0-9] # 筛选列名只有一个数字的列
'''Labels访问loc[]'''


'''聚合函数'''
# count -> Number of non-NA/null observations => 个数
# sum -> Sum of values => 总和
# mean -> Mean of values => 平均值
# median -> Median of values => 中位数
# mode -> Mode of values => 众数
# std -> Standard deviation of the values => 标准差
# var -> Variance of the values => 方差
# min -> Minimum value => 最小值
# max -> Maximum value => 最大值
# prod -> Product of values => 乘积
# cumprod -> Cumulative product of values => 累计乘积
# cumsum -> Cumulative sum of values => 累计总和
# cummin -> Cumulative minimum of values => 累计最小值
# cummax -> Cumulative maximum of values => 累计最大值
# quantile -> Quantile (value at %) => 分位数

import pandas as pd
import numpy as np
df.DataFrame(data=np.random.randint(0, 100, size=(5, 4)), columns=list('ABCD'))
arr_1 = df.values# 转换为NumPy数组
#value != NaN
arr_1.sum(axis = 0)# 按列求和
arr_1.sum(axis = 1)# 按行求和

#避免方法
# pandas 中聚合函数默认会排除 NaN 值
arr1 = arr_1.astype(np.float32)# float = np.float32

np.nansum((arr1), axis=0)# 按列求和 -> 不包含NaN值
np.nansum((arr1), axis=1)# 按行求和

df.loc[1, 'B'] = np.nan# 第2行第2列赋值为NaN
np.sum(df.values)# 所有元素求和 -> 包含NaN值
np.nansum(df.values)# 所有元素求和 -> 不包含NaN值(可直接求值)



'''单层索引  多层索引'''
pd.Index()# 索引对象，用于存储轴标签（行标签、列标签）
RangeIndex(start=0, stop=5, step=1, name = 'index')# 范围索引对象，用于存储轴标签（行标签、列标签）;name 为索引名称
CategoricalIndex(categories=['a', 'b', 'c'], ordered=False)# 分类索引对象，用于存储轴标签（行标签、列标签）
MultiIndex(levels=[['a', 'b'], ['c', 'd']], codes=[[0, 0, 1, 1], [0, 1, 0, 1]])# 多层索引对象，用于存储轴标签（行标签、列标签）
IntervalIndex(start=0, end=5, step=1)# 区间索引对象，用于存储轴标签（行标签、列标签）
DataIndex(start=0, end=5, step=1)# 数据索引对象，用于存储轴标签（行标签、列标签）
Int64Index(start=0, end=5, step=1)# 整数索引对象，用于存储轴标签（行标签、列标签）

df = pd.DataFrame(data = np.random.randint(0, 100, size=(5, 3)), columns = list('ABC'))
df.index# 行索引
df.columns# 列索引
#修改
df.index = ['a', 'b', 'c', 'd', 'e']# 行索引
df.columns = ['1', '2', '3']# 列索引 data = [1, 2, 3]
pd.Index(['a', 'b', 'c', 'd', 'e'])# 行索引
pd.Index(['1', '2', '3'])# 列索引


# 多层索引
#构建
pd.MultiIndex()# 多层索引对象，用于存储轴标签（行标签、列标签）
Level1 = ['第二期', '第二期']
Level2 = ['A', 'B', 'C']
columns = pd.MultiIndex.from_product([Level1, Level2], names=['期数', '产品'])# 使用product()方法创建多层索引
# index = ['Lucy', 'Lily', 'Rose']
index = pd.Index(['Lucy', 'Lily', 'Rose'], name='姓名')
data = np.random.randint(0, 100, size=(3, 6))
df = pd.DataFrame(data=data, index=index, columns=columns)
'''
期数       第一期        第二期        
产品         A   B   C    A   B   C
姓名
Lucy       45  72  18   36  59  81
Lily       23  94  67   12  48  75
Rose       89  31  52   64  27  93
'''

pd.MultiIndex.from_tuples([('a', 'x'), ('a', 'y'), ('b', 'x'), ('b', 'y')])# 使用tuples()方法创建多层索引 -> 二维数组
pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], ['x', 'y', 'x', 'y']])# 使用arrays()方法创建多层索引


# 显示多层索引->元组tuple
# df.loc[row_label, col_labels]
# s.loc[Lables]
# Lables:标签名称 标签名称列表 condition 条件表达式（布尔值） 切片（必须排序） 
df.loc['Lucy', '第二期']# 显示姓名为'Lucy'的第二期数据
df.loc['Lucy', '第二期':'第一期']# 显示姓名为'Lucy'的第二期到第一期数据
df.loc['Lucy', ('第二期', 'A')]# 显示姓名为'Lucy'的第二期产品A数据
df.loc['Lucy', ('第二期', 'A'):'第一期']# 显示姓名为'Lucy'的第二期产品A到第一期数据
df.loc['Lucy', ('第二期', 'A'):'第一期', 'B']# 显示姓名为'Lucy'的第二期产品A到第一期产品B数据
df.loc['第一期']# 显示第一期数据
# 排序
df.sort_index(inplace=True, axis=1)# 按列索引排序; inplace=True 直接在原数据上操作
# 从外围开始，不能越级访问
df.loc['第一期', 'A']# 错误


# 隐式索引访问->整数索引:0->n (左闭右开):1->n
df.iloc[0:4]# 显示第1-4行数据


'''Stack and Unstack'''
# 堆叠:将列索引转换为行索引
df.unstack()# 解堆叠 -> 转换为DataFrame; 行索引转为列索引
df.stack()# 堆叠 -> 转换为Series; 列索引转为行索引
df.stack().index# 堆叠后的索引
df.stack().unstack()# 解堆叠 -> 转换为DataFrame
# Level:自value开始计算，向左为-1, 向右为0->n-1
df.stack().unstack(level=0)# 解堆叠 -> 转换为DataFrame, 0为列索引, 1为行索引
df.stack().unstack(level=1)# 解堆叠 -> 转换为DataFrame, 0为列索引, 1为行索引


'''数据IO操作 -> 读取有特定格文件'''
fp = open('city.csv', 'r', encoding='utf-8', errors='ignore')# 打开文件, 读取模式, 编码为utf-8, 忽略错误
fp.read()# 读取文件内容
fp.close()# 关闭文件

# 读取文件为一次性操作，再次读取需要重新打开文件
fp = open('city.csv', 'r', encoding='utf-8', errors='ignore')# 打开文件, 读取模式, 编码为utf-8, 忽略错误
fp.read()# 读取文件内容
fp.close()# 关闭文件

# pandas 读取csv、txt文件
pd.read_csv('city.csv',  sep=',', header=None, index_col=0)# 读取xx.csv文件, (默认)分隔符为',', 无表头, 第1列作为行索引
pd.read_table('city.txt', sep='\t', header=None, index_col=0)# 读取xx.txt文件, (默认)分隔符为'\t', 无表头, 第1列作为行索引
# 方法一致，仅分隔符不同
sep='\s+'# 空格分隔符, 多个空格为一个分隔符


'''EXCEL文件读取'''
# excel自带索引n行, 从第1行开始读取数据
data = pd.read_excel('Names.xlsx', sheet_name='Sheet1', index_col=0, header=None, names=['姓名', '年龄', '性别'])# 读取xx.xlsx文件, 第1张工作表, 第1列作为行索引, 无表头, 自定义表头, 姓名、年龄、性别
# sheet_name:工作表名称,可以为字符串、整数、列表

# read
data.to_excel('Names.xlsx', sheet_name='Sheet1', index=False)# 写入xx.xlsx文件, 第1张工作表, 无索引
data.read_csv('Names.csv', sep=',', header=None, index_col=0, names=['姓名', '年龄', '性别'])# 读取xx.csv文件, 第1张工作表, 第1列作为行索引, 无表头, 自定义表头, 姓名、年龄、性别


'''数据探索'''
data.describe(percentiles=[0.25, 0.5, 0.75])# 描述性统计,percentlist(default=[0.25, 0.5, 0.75])
# return:数值型数据的列统计信息;.T转置，方便查看
# count:非空值数量
# mean:平均值
# std:标准差
# min:最小值
# 25%:25%分位数
# 50%:50%分位数（中位数）
# 75%:75%分位数
# max:最大值

info = data.info()# 数据信息
# return:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1000 entries, 0 to 999
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   姓名      1000 non-null   object
#  1   年龄      1000 non-null   int64
#  2   性别      1000 non-null   object
# dtypes: int64(1), object(2)
# memory usage: 23.6+ KB

head = data.head()# 显示前5行数据
# return:
#    姓名  年龄  性别
# 0  张三  25  男
# 1  李四  30  女
# 2  王五  28  男
# 3  赵六  35  女
# 4  王二  22  男

tail = data.tail()# 显示后5行数据
# return:
#     姓名  年龄  性别
# 995  王二  22  男
# 996  张三  25  男
# 997  李四  30  女
# 998  王五  28  男
# 999  赵六  35  女

sample = data.sample(5)# 随机抽取5行数据
# return:
#     姓名  年龄  性别
# 523  王二  22  男
# 722  张三  25  男
# 475  李四  30  女
# 888  王五  28  男
# 244  赵六  35  女


# 常用数据处理函数
# 假设 data 是 DataFrame 或 Series
data.mean()      # 平均值
data.median()    # 中位数
data.mode()      # 众数
data.sum()       # 总和
data.std()       # 标准差
data.var()       # 方差
data.describe()  # 生成综合统计报告（包含以上所有）

data.min()       # 最小值
data.max()       # 最大值
data.idxmin()    # 最小值的索引位置
data.idxmax()    # 最大值的索引位置

data.quantile(0.25)  # 25% 分位数（下四分位）
data.quantile(0.5)   # 50% 分位数（中位数）
data.quantile(0.75)  # 75% 分位数（上四分位）
data.quantile([0.1, 0.5, 0.9])  # 同时计算多个分位数

data.cumsum()    # 累计求和
data.cumprod()   # 累计乘积
data.cummax()    # 累计最大值
data.cummin()    # 累计最小值

data.count()       # 非空值数量
data.value_counts() # 每个值出现的频率（仅 Series 可用）
data.nunique()     # 唯一值的数量

data.corr()       # 相关系数矩阵（仅 DataFrame）
data.cov()        # 协方差矩阵（仅 DataFrame）
data.corrwith(other_data)  # 与另一数据集的相关性


import numpy as np
np.mean(arr)    # 数组平均值
np.median(arr)  # 数组中位数
np.std(arr)     # 数组标准差
np.var(arr)      # 数组方差



'''空值处理'''
# python中None表示缺失值, 与np.nan不同, None是python的关键字, 而np.nan是numpy的缺失值表示
# int < float < complex
# 数值类型 < datetime64 < timedelta64


'''None'''
# Type: NoneType; 不参与计算
# 缺失值处理
data.dropna()  # 删除包含缺失值的行
data.fillna(value)  # 用指定值填充缺失值
data.isnull()  # 检测缺失值（返回布尔掩码）
data.notnull()  # 检测非缺失值（返回布尔掩码）

def get_sum(x):
    return x.sum()

datal = np.arange(100000, dtype=object)# 生成100000个元素的数组, 元素类型为object
# %time get_sum(datal)# 统计用时（Python终端中操作，非code）
# %timeit get_sum(datal)# 统计用时均值（Python终端中操作，非code）


'''NaN'''
np.nan(NaN)
# Type: numpy float; 参与计算
# 缺失值处理
data.dropna()  # 删除包含缺失值的行
data.fillna(value)  # 用指定值填充缺失值
data.isnull()  # 检测缺失值（返回布尔掩码）
data.notnull()  # 检测非缺失值（返回布尔掩码）

# pandas自动将None处理为np.nan


'''空值查找'''
isnull = data.isnull()# 检测缺失值（返回布尔掩码）
notnull = data.notnull()# 检测非缺失值（返回布尔掩码）
df = pd.DataFrame(data=np.random.randint(size=(10, 4)), columns=['A', 'B', 'C', 'D'])
df.loc[2] = np.nan# 第2行所有元素设为np.nan
df.loc[4, 'B'] = np.nan# 第4行B列设为np.nan
df.loc[5, 'D'] = np.nan# 第5行D列设为np.nan
df.loc[9, ['A', 'B']] = np.nan# 第9行A、B列设为np.nan


df.isnull()# 检测缺失值（返回布尔掩码）
# 检查缺失值
# any()：有False = False -> 检查是否有缺失值（返回布尔值）
# all()：全为True = True -> 检查是否所有值都是缺失值（返回布尔值）
df.isnull().sum().any()# 检查每列是否有缺失值(sum()列方向和)
# 通过any(axis=n)定位缺失值
df.isnull().any(axis=1)# 检查每行是否有缺失值(axis=1->检查每行是否有缺失值)
df.isnull().any(axis=0)# 检查每列是否有缺失值(axis=0->检查每列是否有缺失值)


# 检查非缺失值
df.notnull().sum().all()# 检查每列是否有非缺失值(sum()列方向和)
#找出全部不为空的行
df.loc[df.notnull().all(axis=1)]


np.array([True, False, True, False].astype(int))# 转换为整数int类型
# replace: np.float
# 利用运算进行缺失值处理：强制转换，低优先级->高优先级
# 1. 缺失值（np.nan）参与计算时，结果为np.nan
# 2. 缺失值与非缺失值进行计算时，缺失值会被转换为非缺失值的类型
# 3. 缺失值与0进行计算时，缺失值会被转换为0
# 4. 缺失值与1进行计算时，缺失值会被转换为1
np.array([True, False, True, False])*1# BOOL与1进行计算时，BOOL值会被转换为1
np.array([True, False, True, False]).mean()# BOOL计算时，BOOL值会被转换为1, 所以平均值为0.5

df.isnull().mean()# 检查每列缺失值比例

'''空值处理'''
# 统一填充
df.fillna(value=0)# 用0填充缺失值
# 均值
df.fillna(df.mean())# 用每列均值填充缺失值
# 自身填充，无需value
df.fillna(method='backfill', axis=1, limit=1)# 用后一个非缺失值填充缺失值, axis=0->按列填充, axis=1->按行填充, limit=1->只填充1个缺失值
# method=
# 'ffill'/'pad'：用前一个非缺失值填充缺失值
# 'bfill'/'backfill'：用后一个非缺失值填充缺失值


'''空值过滤'''
# 过滤出所有非缺失值的行
df.loc[df.notnull().all(axis=1)]# 过滤出所有非缺失值的行
# 过滤出D列非缺失值的行
df.loc[df['D'].notnull()]


df.dropna(axis=0, how='any', thresh=2, subset=['A', 'B'], inplace=True)
# how:
# 'any'：如果有缺失值，就删除这一行
# 'all'：如果所有值都是缺失值，就删除这一行
# thresh: 保留至少n个非缺失值的行
# subset: 仅在指定列中检查缺失值(子集)
# inplace: 是否在原数据上操作, True->在原数据上操作, False->返回新的DataFrame



'''异常值处理'''
# describe()：描述性统计（包括异常值）,查看每一列描述性统计
'''异常值分析'''
# 认定异常值：
# 1. 超出正常范围的数值（如：温度超过30℃）
# 2. 与其他数据明显不同的数值（如：一个人年龄为120岁）
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline# Jupyter 中有效：图表直接显示在单元格中

# 创建图表代码
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='日期', y='销售额')
plt.title('销售额趋势图')

# 显示图表（必须添加）
plt.show()


# 不符合业务逻辑的异常值

# 使用均值和标准差进行判断
# abs(X) > 3*X.std()# 3倍标准差外的数值
'''数据满足标准正态分布'''

pd.DataFrame(np.random.randn(1000, 4), columns=['A', 'B', 'C', 'D'])# 生成1000个标准正态分布随机数
sns.histplot(df['A'], kde=True)# 绘制A列的直方图, kde=True->添加核密度估计曲线
plt.title('A列标准正态分布直方图')
plt.show()
# 生成直方图
df.std()# 计算每列标准差 +-3倍标准差内的数值为99.7%
# 大于3倍标准差的数值为异常值
exp_condition = (np.abs(df) > 3*df.std()).any(axis=1)# 3倍标准差外的数值 -> Bool
df.loc[exp_condition]# 3倍标准差外的数值
normal_condition = (np.abs(df) <= 3*df.std()).all(axis=1)# 正常数值 -> Bool
df.loc[normal_condition]# 正常数值
# 过滤
ex_index = df.loc[exp_condition].index# 3倍标准差外的数值索引
df.loc[ex_index]# 3倍标准差外的数值
df.drop(index=ex_index, inplace=True)# 删除3倍标准差外的数值



# 使用上四分位数和下四分位数进行判断
df.describe(percentiles=[0.25, 0.75])# 描述性统计（包括异常值）,查看每一列描述性统计
# 中间50%的数据
Q1 = df.quantile(0.25)# 下四分位数-25%
Q3 = df.quantile(0.75)# 上四分位数-75%
IQR = Q3 - Q1# 四分位范围
bottom = Q1 - 1.5*IQR# 下边界-1.5倍IQR
upper = Q3 + 1.5*IQR# 上边界+1.5倍IQR
exp_condition = (df < bottom) | (df > upper)# 异常值条件
df.loc[exp_condition]# 异常值
normal_condition = ~exp_condition# 正常数值条件
df.loc[normal_condition]# 正常数值

order = pd.read_excel('order.xlsx')# 读取订单数据
order.info()# 查看订单数据信息, info()方法可以查看数据的基本信息, 包括列名、非缺失值数量、数据类型等
order.describe(percentiles=[0.25, 0.75, 0.99])# 查看订单数据描述性统计, 包括计数、均值、标准差、最小值、25%、50%、75%、最大值
sns.boxplot(data=order, x='订单状态', y='订单金额')# 绘制订单状态与订单金额的箱线图
plt.title('订单状态与订单金额的箱线图')
plt.show()

Q1, Q2 = np.quantile(order['订单金额'], q=[0.25, 0.75])# 计算订单金额的下四分位数和上四分位数
IQR = Q3 - Q1# 计算订单金额的四分位范围
Bottom = Q1 - 1.5*IQR# 下边界-1.5倍IQR
Upper = Q3 + 1.5*IQR# 上边界+1.5倍IQR

# filter()方法可以根据条件筛选数据
(order['订单金额']).values
condition = (order[order['订单金额'] >= Bottom or order['订单金额'] <= Upper])# 筛选出订单金额大于等于下边界或小于等于上边界的订单
exp_index = order.loc[condition].index# 筛选出订单金额大于等于下边界或小于等于上边界的订单索引
order.drop(index=exp_index, inplace=True)# 删除订单金额大于等于下边界或小于等于上边界的订单



'''重复值处理'''
df = pd.DataFrame({
    'A': [1, 2, 2, 3, 4, 4, 4],
    'B': ['a', 'b', 'b', 'c', 'd', 'd', 'd']
})# 创建包含重复值的DataFrame

# 查找重复值
df.duplicated(keep='first', subset=['A'])# 查找重复值(首次出现为False, 后续重复为True)（返回布尔掩码）
# keep 参数:
# 'first'：标记除首次出现外的重复值为 True
# 'last'：标记除最后一次出现外的重复值为 True
# False：将所有重复值都标记为 True

# 删除重复值
condition = df.drop_duplicates(inplace=True)# 删除重复值（在原数据上操作）
# 取反操作
df[~df.duplicated(keep='first', subset=['A'])]# 取反操作, 保留首次出现的重复值
# ~ 取反操作, 保留首次出现的重复值
(condition - 1).astype(bool)# 取反操作, 保留首次出现的重复值
# bool与int类型运算时, True=1, False=0
# bool(1 / 0) ->仅能够转换int类型的数值


'''pandas排序与随机抽样'''
sort_index = df.sort_index(by=['A', 'B'], axis=0, ascending=True)# 按行索引排序, axis=0->按行排序, axis=1->按列排序, ascending=True->升序, ascending=False->降序
# by:排序依据列名列表
# ['列名1', '列名2'] -> 先按列名1排序, 相似时, 再按列名2排序

df.sort_index(by=['A', 'B'], axis=0, ascending=False)# 按行索引排序, axis=0->按行排序, axis=1->按列排序, ascending=True->升序, ascending=False->降序
# by:排序依据列名列表
# ['列名1', '列名2'] -> 先按列名1排序, 相似时, 再按列名2排序

df.sample(n=3, axis=0, replace=False, random_state=42)# 随机抽样, n=3->抽样数量, replace=False->不放回抽样, random_state=42->随机种子

df.take(indices=[0, 2, 4], axis=0)# 按位置索引抽样, indices=[0, 2, 4]->抽样位置索引列表, axis=0->按行抽样, axis=1->按列抽样
# indices:位置索引列表 -> [位置索引1, 位置索引2, 位置索引3],可与axis设置联合使用更改列或行排序



'''索引操作'''
# 将指定列设置为索引（字段）
df.set_index(keys=['A', 'B'], drop=True, append=False, inplace=False)# 设置索引, keys=['A', 'B']->索引列名列表, drop=True->删除原索引列, append=False->不追加原索引列, inplace=False->返回新的DataFrame

# 将指定索引转换为列（字段）
df.reset_index(level=None, drop=False, inplace=False)# 重置索引, level=None->重置所有索引, drop=False->不删除原索引列, inplace=False->返回新的DataFrame
# level:指定重置的索引级别, 可为整数、字符串或列表

# 重新索引(填充缺失值)
df.reindex(labels=None, index=None, columns=None, axis=None, method=None, fill_value=None, limit=None, tolerance=None)# 重新索引, labels=None->新索引标签列表, index=None->新行索引标签列表, columns=None->新列索引标签列表, axis=None->轴方向, method=None->填充方法, fill_value=None->填充值, limit=None->填充限制, tolerance=None->容差
# labels:新索引标签列表, 可与axis设置联合使用更改列或行索引

# 删除指定级别的索引
df.droplevel(level=0, axis=0)# 删除指定级别的索引, level=0->索引级别, axis=0->按行删除, axis=1->按列删除
# level:指定删除的索引级别, 可为整数、字符串或列表


'''映射处理'''
df.rename(mapper=None, index=None, columns=None, axis=None, inplace=False)# 重命名索引或列, mapper=None->映射字典或函数, index=None->行索引映射字典或函数, columns=None->列索引映射字典或函数, axis=None->轴方向, inplace=False->返回新的DataFrame
# mapper:映射字典或函数, 可与axis设置联合使用更改列或行索引
df.rename(mapper=lambda x: str(x)+'_new', axis=1, inplace=True)# 列名添加后缀_new

dic = {
    'a': 'A_new',
    'b': 'B_new'
}
df.rename(mapper=dic, axis=0, inplace=True)# 行索引重命名, 未在字典中的索引保持不变

# replace()方法可以替换指定的值
df = pd.DataFrame(np.random.randint(0, 100, size=(5, 4)), columns=['A', 'B', 'C', 'D'])

# list方式替换
df.replace(to_replace=[50, 60], value=[100, 200], inplace=True)# 将所有50和60替换为100和200
# to_replace:要替换的值列表
# value:替换后的值列表

# dict方式替换
df.replace(to_replace={40: 110, 55: 230}, inplace=True)# 将所有50替换为100, 60替换为200

#dict特殊方式替换
df.replace(to_replace=['A':'Hello'], value='hELLO', inplace=True)# 将所有"不及格"替换为np.nan
# to_replace:要替换的值字典, key为要替换的值, value为替换后的值
# 特殊情况: key为列名, value为替换后的值, 则会将该列中所有值为key的元素替换为value
df.replace(to_replace={'A': [1, 2]}, value=np.nan, inplace=True)# 将A列中所有1替换为100, 2替换为200

# regex方式替换
df.replace(to_replace=r'^A.*', value='StartsWithA', regex=True, inplace=True)# 将所有以A开头的字符串替换为'StartsWithA'
# regex:是否使用正则表达式进行替换, 默认False
# True: 使用正则表达式进行替换
# False: 不使用正则表达式进行替换

# 正则表达式:
# ^A.*: 以A开头的字符串
# r'^A.*': 以A开头的字符串, 忽略大小写
# .*A$: 以A结尾的字符串
# .*A.*: 包含A的字符串
# ?A.*: 以A开头, 且后面跟着任意字符的字符串

#method方式替换
df.replace(to_replace=[1, 2, 3], method='bfill', limit=1, inplace=True)# 将所有1、2、3替换为后一个非缺失值


'''map()方法'''
df.A == df['A'] == df.loc[:, 'A']# 访问A列数据

df.A.replace(to_replace={1: 'One', 2: 'Two', 3: 'Three'}, inplace=True)# 将A列中的1、2、3替换为'One'、'Two'、'Three'
# replace()方法可以用于Series对象, 也可以用于DataFrame对象

df['A'] = df['A'].map({1: 'One', 2: 'Two', 3: 'Three'})# 将A列中的1、2、3替换为'One'、'Two'、'Three'
# map()方法只能用于Series对象, 不能用于DataFrame对象

D = df['D']
D.map(lambda x: x**2)# 对D列中的每个元素进行平方操作
# function: 函数对象, 对每个元素进行操作
# dict: 映射字典, key为要替换的值, value为
# Series: 映射Series, index为要替换的值, values为替换后的值

def score_map(x):
    if x >= 90:
        return '优秀'
    elif x >= 80:
        return '良好'
    elif x >= 70:
        return '中等'
    elif x >= 60:
        return '及格'
    else:
        return '不及格'

# 模糊匹配
D.map(score_map)# 对D列中的每个元素进行成绩等级划分
# score_map: 自定义函数, 对每个元素进行操作; 非score_map()调用，而是传入函数对象

def map_function(D):
    re_value = []
    for x in D:
        v = score_map(x)
        re_value.append(v)
    return re_value

# 精确匹配
map_dic = {
    95: '优秀',
    85: '良好',
    75: '中等',
    65: '及格',
    55: '不及格'
}
D_re =D.map(map_dic)

df = pd.DataFrame(data=np.random.randint(0, 100, size=(3, 2)), columns=['A', 'B'])
df.A.replace(to_replace={0: 'Zero', 1: 'One'}, inplace=True)# 将A列中的0、1替换为'Zero'、'One'
map_dict2 = {
    'Zero': True,
    'One': False
}
# get() -> dict
map_dict2.get('A', "a")# 获取key为'A'的值, 如果不存在则返回默认值"a"

def map_dict2_function(x):
    return map_dict2.get(x, x)# 获取key为x的值, 如果不存在则返回x本身

D_re2 = df.A.map(map_dict2)# 将A列中的'Zero'、'One'替换为True、False
# 未匹配到的值会被替换为NaN
D_re2 = df.A.map(map_dict2_function)# 将A列中的'Zero'、'One'替换为True、False
# 未匹配到的值保持不变




'''Pandas高级数据处理'''
'''级联'''
# 级联核心:索引对齐
# 应用场景:不同期、结构相同的数据合并
# numpy: np.concatenate()
# pandas: pd.concat()
import numpy as np
import pandas as pd

# numpy中的级联
np.concatenate((arr_1, arr_2), axis=0)# 按行级联 -> axis=0 按行级联; axis=1 按列级联
np.concatenate((arr_1, arr_2), axis=1)# 按列级
# 必须保证维度一致

# pandas中的级联
pd.concat([df1, df2], axis=0, ignore_index=True)# 按行级联 -> axis=0 按行级联; axis=1 按列级联; ignore_index=True 重置索引
pd.concat([df1, df2], axis=1)# 按列级联 -> axis=1 按列级联; ignore_index=True 重置索引
# 必须保证索引一致

df_1 = pd.DataFrame(data=[[1, 2, 3]], columns=list('ABC'))# 创建DataFrame
# [[1, 2, 3]] -> 1行3列 2维数组
df_2 = pd.DataFrame(data=[[2, 3, 4]], columns=list('ABC'))# 创建DataFrame
# [[2, 3, 4]] -> 1行3列 2维数组
pd.concat([df_1, df_2], axis=0)# 按行级联 -> axis=0 按行级联; ignore_index=True 重置索引
#    A  B  C
# 0  1  2  3
# 0  2  3  4
# 重复索引

# 校验索引是否重复
pd.concat([df_1, df_2], axis=0).index.is_unique# False
pd.concat([df_1, df_2], axis=0, verify_integrity=True)# 校验索引是否重复, 无重复则返回None, 有重复则报错

# 变为多层索引
pd.concat([df_1, df_2], axis=0, keys=['期数1', '期数2'], names=['期数', '产品'])# 按行级联 -> axis=0 按行级联; keys=['期数1', '期数2']->多层索引
#           A  B  C 
# 期数    产品
# 期数1  0  1  2  3
# 期数2  0  2  3  4

# 忽略索引
pd.concat([df_1, df_2], axis=0, ignore_index=True)# 按行级联 -> axis=0 按行级联; ignore_index=True 重置索引

df1 = pd.DataFrame(data=np.random.randint(0, 10, size=(3, 3)), columns=['A', 'B', 'C'])# 创建DataFrame
df2 = pd.DataFrame(data=np.random.randint(10, 20, size=(3, 4)), columns=['A', 'B', 'C', 'D'])# 创建DataFrame
 # 按列级联
pd.concat([df1, df2], axis=1, sort=False)# 按列级联 -> axis=1 按列级联; sort=False 不排序(按列索引排序)
# 索引不匹配时, 以df1为准, df2缺失值补NaN

df3 = pd.DataFrame(data=np.random.randint(0, 100, size=(3, 4)), columns=['A', 'B', 'C', 'D'])# 创建DataFrame
df4 = pd.DataFrame(data=np.random.randint(-100, 0, size=(4, 3)), columns=[ 'B', 'D', 'E'])# 创建DataFrame
display(df3, df4)
pd.concat([df3, df4], axis=0, sort=True, join='inner')# 按行级联 -> axis=0 按行级联; sort=True 排序(按列索引排序)
# join:index排列
# 'inner'：取交集
# 'outer'：取并集


'''合并'''
# 合并核心:指定列对齐(仅支持2个表合并):一对一、一对多、多对多，否则结果为空
# 应用场景:不同结构、不同期的数据合并:离散型（可以是数值型）
# numpy: np.merge()
# pandas: pd.merge()
import numpy as np
import pandas as pd
# numpy中的合并
np.merge(arr_1, arr_2, on=0, how='inner')#
# on=0->按第1列对齐; on=1->按第2列对齐
# how='inner'：取交集
# how='outer'：取并集

# pandas中的合并
pd.merge(df1, df2, on='key', how='inner')# 按key列对齐, 取交集
pd.merge(df1, df2, on='key', how='outer')# 按key列对齐, 取并集
pd.merge(df1, df2, left_on='key1', right_on='key2', how='inner')# 按key1列对齐, 取交集
# left_on='key1'：左表对齐列
# right_on='key2'：右表对齐列

# 合并示例
df_1 = pd.DataFrame(data={'key': [1, 2, 3], 'value': [4, 5, 6]}, columns=['key', 'value'])# 创建DataFrame
df_2 = pd.DataFrame(data={'key': [2, 3, 4], 'value': [7, 8, 9]}, columns=['key', 'value'])# 创建DataFrame
pd.merge(df_1, df_2, on='key', how='inner')# 按key列对齐, 取交集
#    key  value_x  value_y
# 0    2        5        7
# 1    3        6        8


'''多sheet Excel文件读取'''
UserID = pd.read_excel('order_data.xlsx', sheet_name=0)# 读取Excel文件, 第1张工作表
UserID.head()# 显示前5行数据
product_table = pd.read_excel('order_data.xlsx', sheet_name=1)# 读取Excel文件, 第2张工作表
first_half_year = pd.read_excel('order_data.xlsx', sheet_name=2)# 读取Excel文件, 第3张工作表
last_half_year = pd.read_excel('order_data.xlsx', sheet_name=3)# 读取Excel文件, 第4张工作表
return_table = pd.read_excel('order_data.xlsx', sheet_name=4)# 读取Excel文件, 第5张工作表

# merge合并默认方式为inner,默认合并相同字段名称列
res1 =pd.merge(left=first_half_year, right=product_table, on='订单ID', how='outer')# 按订单ID列对齐, 取并集
res1['订单总额'] = res1['购买数量']*res1['单价']# 计算购买数量*单价, 得到订单总额并存为新列
res1['订单总额'].sum()# 计算订单总额列的总和

res2 = pd.merge(left=first_half_year, right=UserID, on='userID', how='left')# 按订单ID列对齐, 以res1为主表, 左连接return_table
# how='left'：左连接
# how='right'：右连接
# default='inner'：内连接

value_counts(res2['性别'])# 统计性别列的值频率


# merge多对多合并
pd.merge(left=first_half_year, right=last_half_year, on=['订单ID'], suffixes=['_上半年', '_下半年'], how='inner')# 按订单ID列对齐, 取交集
# 多对多合并会产生笛卡尔积, 导致数据量激增
# on=['']：多个相同字段中，指定合并要参考的字段列表
# suffixes=['', '']：为名称相同且未参与合并的列添加后缀


# 未存在相同字段合并
pd.merge(lest=first_half_year, right=return_table, left_on='订单ID', right_on='订单_id', how='left')# 按订单ID列对齐, 以first_half_year为主表, 左连接return_table

# left_index\right_index:合并后索引 -> ignore_index=True时无效(重现排布)


'''分组'''
# 分组必聚合:分组依据+聚合函数
# 应用场景:分类汇总、透视分析
groupby = data.groupby(by='key')# 按key列分组
groupby['value'].sum()# 对value列进行求和聚合

df = pd.read_excel('menu_table.xlsx', index_col=0)
# index_col=0 表示第1列作为索引
df.groupby(by=['菜品']).groups# 按菜品列分组, 查看分组情况(分组行索引)
# {'鱼香肉丝': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], '红烧肉': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], '青椒肉丝': [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]}
# 查看
df.loc[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]# 鱼香肉丝数据

# DataFrameGroupBy对象可直接调用pandas聚合函数
df.groupby(by=['菜品']).sum()# 按菜品列分组, 对其他列进行求和聚合
# 单独处理:DataFrame -> Series
df.groupby(by=['菜品'])['数量'].sum()# 按菜品列分组, 对数量列进行求和聚合 only one column
df.groupby(by=['菜品']).sum()['数量']# 按菜品列分组, 对数量列进行求和聚合 all columns then select one

df.groupby(by=['菜品'])['价格'].mean()# 按菜品列分组, 对价格列进行平均值聚合

df.groupby(by=['菜品'])['数量'].max()# 按菜品列分组, 对数量列进行最大值聚合
df.groupby(by=['菜品'])['数量'].min()# 按菜品列分组, 对数量列进行最小值聚合

df.groupby(by=['菜品'])['数量'].std()# 按菜品列分组, 对数量列进行标准差聚合
df.groupby(by=['菜品'])['数量'].var()# 按菜品列分组, 对数量列进行方差聚合

df.groupby(by=['菜品'])['数量'].describe()# 按菜品列分组, 对数量列进行综合统计报告聚合

df.groupby(by=['菜品'])['数量'].agg(['sum', 'mean', 'max', 'min'])# 按菜品列分组, 对数量列进行多种聚合

# 多分组
# 制定多种聚合指标
gpobj = df.groupby(by=['菜品'])
# agg()方法可以同时对多列进行多种聚合操作
gpobj.agg({
    '数量': ['sum', 'mean', 'max', 'min'], 
    '价格': 'mean'
    })# 按菜品列分组, 对数量列进行多种聚合, 对价格列进行平均值聚合
# keys:指定分组依据列 必须与groupby(by=[])分组中列名一致
# values:指定聚合函数列表 或 单个聚合函数
gpobj.agg({
    '数量': np.sum, 
    '价格': np.mean
    })# 按菜品列分组, 对数量列进行求和聚合, 对价格列进行平均值聚合

df.groupby(by=['菜品', '颜色'])['价格'].mean().unstack()# 按菜品和颜色列分组, 对价格列进行平均值聚合
# unstack()方法可以将多级索引转换为列索引

# 高级聚合
df.groupby('菜品')['数量'].mean()# 按菜品列分组, 对数量列进行平均值聚合
df.groupby('菜品')['数量'].apply(lambda x: x.mean())# 按菜品列分组, 对数量列进行自定义聚合
# lambda x: x.mean() -> 自定义聚合函数, 对每个分组进行操作 == np.mean(x)


'''交叉表'''
# 统计数量 count
df.groupby(by=['菜品', '颜色'])['数量'].count().unstack()# 按菜品和颜色列分组, 对数量列进行计数聚合
pd.crosstab(index=df['菜品'], columns=df['颜色'])# 交叉表, 统计菜品和颜色的数量分布
# index:必须是序列或数组,[]


'''透视表'''
# 统计汇总 sum、mean等
## 需要指定index、columns、values等数据源
pd.pivot_table(data=df, index='菜品', columns='颜色', values='数量', aggfunc='sum', fill_value=0)# 透视表, 按菜品和颜色列分组, 对数量列进行求和聚合, 缺失值填充为0
