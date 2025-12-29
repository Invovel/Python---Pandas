print()#打印

'''变量'''
a = 3
#整数
int()
#浮点型
float(a)#3.0
#字符型
String > str()
#布尔值
BOOR > True / False
#复数
complex()#4+3j 4+3J  => z.real  z.imag

print(type(a))#type()查看

'''input()'''
input()#-> String
pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_by_second = sorted(pairs, key=lambda x: x[1])
print(sorted_by_second)  # 输出: [(2, 'a'), (1, 'b'), (3, 'c')]
seconds = [x[1] for x in pairs]
print(seconds)  # 输出: ['b', 'a', 'c']
input().split()#分隔
map(int,input())#->List

'''注释'''
# -> single
''''''# -> numcial
Str = '''
        x
        y
        z
'''#str

'''计算'''
'''+ - * / // % **
=='''

'''格式化'''
print("%s is %d years old. "%(name, age))
print("{} is {} years old.".format(name, age))
print(f"{name} is {age} years old.")#f-string -> f/F"{}"
'''conversion
f'{!s（str）、!r（repr）、!a（ascii）}' 
f"{expr=}" == expr=value

[fill][align][sign][#][0][width][grouping_option][.precision][type]
fill + align: 填充与对齐，< 左、> 右、^ 居中、= 数字在符号后填充。如 f"{s:*^10}"。
sign: +、-、 （空格）控制正负号显示。
#: 备用格式，整数类型会带前缀（0b/0o/0x）。
0: 零填充（如 f"{n:08d}"）。
width: 最小宽度（如 f"{x:6}"）。
grouping_option: ,（千位逗号）或 _（下划线分组），如 f"{1000000:,}" → 1,000,000。
.precision: 精度，对于浮点 f 是小数位数，对 g 是有效数字，对字符串是截断长度（如 f"{pi:.2f}"）。
type: 格式类型，常见有：
整数：d（十进制）、b（二进制）、o（八进制）、x/X（十六进制）
浮点：f、F、e、E、g、G、%（乘 100 并加 %）
n：按当前区域格式化数字
示例： f"{value:0>8.2f}"、f"{num:+08d}"、f"{text:.5}"。

快速示例:

基本： f"Hello, {name}!"
数字与宽度： f"{n:08d}" -> 零填充到 8 位
小数精度： f"{pi:.3f}" -> 保留 3 位小数
千位分隔： f"{1000000:,}" -> 1,000,000
进制与前缀： f"{15:#x}" -> 0xf
日期： f"{dt:%Y-%m-%d}"
转换： f"{obj!r}" -> 使用 repr(obj)
调试： f"{a + b=}" -> 输出 a + b=42
'''

'''format 类型（type）与简短示例。'''

# 整数类型
# b：二进制（例：f"{15:b}" → 1111）
# c：整数对应的 Unicode 字符（例：f"{65:c}" → A）
# d：十进制（例：f"{123:d}" → 123）
# o：八进制（例：f"{8:o}" → 10）
# x / X：十六进制（小/大写字母，例：f"{255:#x}" → 0xff，f"{255:#X}" → 0XFF）
# n：按当前区域（locale）格式化数字（例：f"{1000:n}"）

# 浮点/科学计数
# f / F：定点表示（例：f"{3.14159:.2f}" → 3.14）
# e / E：指数表示（例：f"{1234.5:e}" → 1.234500e+03）
# g / G：通用格式（在定点/指数间自动选择，例：f"{0.00012345:g}"）
# %：乘以100并以 % 显示（例：f"{0.1234:%}" → 12.340000%）

# 字符串
# s：字符串表示（例：f"{obj:s}"，通常默认行为相当于 s）

# 其他常用配合项（不是类型，但常用）
# #：备用格式（对整数在 b/o/x 前加 0b/0o/0x）
# 0、width、fill、align、.precision：控制宽度、填充、对齐与精度（例：f"{pi:06.2f}" → 宽度6、零填充、保留2位）
# 分组：,（千位逗号），_（下划线分组），例：f"{1000000:,}" → 1,000,000
# 转换标志（conversion）：!s、!r、!a（在 : 之前使用，如 f"{obj!r}"）
# 调试语法（Python 3.8+）：f"{expr=}" 或带格式 f"{expr=:05.1f}"
# 自定义类型

# 格式化会调用对象的 __format__(self, spec)，自定义对象可实现自己的格式化行为。

'''内置运算符'''
abs()#绝对值
divmod(a,b)#商和余数
pow(a,b)#a的b次方  pow(n,pow(x,y)) == x**(y*n)  
round(a,n)#四舍五入 n位小数
sum()#求和
'''->list 
lst = [1,2,3,4,5]
i, n = 1, 2
sum(lst[i:i+n])     # 2 + 3 = 5
sum(lst[i:i+n+1])   # 2 + 3 + 4 = 9  （包含 i+n）
sum(range(1, 3+1))  # 1+2+3 = 6'''

max()#最大值
min()#最小值
# \t制表符
# \n换行符
"xxx,end=''"#print不换行
print( f"{4.3e2}", end='\t')#


4.3e2#科学计数法 4.3*10^2

'''加空格的条件表达式'''
# 缩进: 代码块用一致缩进（PEP8 建议四个空格），用于 if/for/while/def/class 等。
# 操作符周围加空格: 二元操作符前后各一个空格，例如 a + b、x == y（但函数调用、索引、切片的括号/方括号内部不要多余空格）。
# 条件表达式: 三元写法为 x if condition else y，if/else 两侧用空格以保持可读。
# 逗号后加空格（列表/元组/参数等）: 列表、元组、参数等逗号后加空格：a, b, c；括号内不要在开头/结尾加空格：func(a, b), [(1, 2), (3, 4)]。
# 关键字参数赋值: 函数调用或定义中关键字参数的等号两侧不加空格：func(a=1, b=2)；但普通赋值语句要用空格：x = 1。
# 切片/索引: 切片内不加空格：seq[start:stop] 而不是 seq[ start : stop ]。
# 默认/特殊情况: 对齐/对齐填充、注释前后等有额外约定，但以上为最常见的空格规则。
if a <= x < b:
        print("In range")
elif a > b:
        print("a is greater") 
else:
        print("b is greater or equal")

'''循环逻辑'''
# 语法：for var in iterable: / while condition:，后接缩进的循环体（PEP8 建议 4 空格）。
# 可迭代对象：支持 list/tuple/str/dict/set/range/generator 等。
# 索引/并行：enumerate(seq) 获取索引，zip(a,b) 并行遍历。
# 字典遍历：for k in d (键)、for v in d.values()、for k,v in d.items()。
# 解包：for a,b in pairs:（结构需匹配）。
# 禁忌：不要在遍历时修改同一序列（用切片拷贝或列表推导替代）。
# 控制流：break 终止，continue 跳过当前，pass 占位。
# else 子句：for/while ... else 在未触发 break 时执行 else 块。
# 性能/习惯：用 range/生成器节约内存；复杂逻辑放函数；优先使用列表推导或生成器表达式。
for i in range(5, 10, 2):#5:begin 10:end 2:step
    print(i)
for _ in "hello":
    print("Hi" + _) 
    print(f"Hi{_}")

'''函数'''
def func_name(params, factor = value_default):
    '''docstring'''
    # code
    return value

def func_name(params): return value #单行函数

def func_name(): 
    global a = input()
    b = input()
    return a + b
#调用
result = func_name()
x, y = func_name()#多个返回值

def func_name(*args, **kwargs): # *args: 可变位置参数(元组tuple), **kwargs: 可变关键字参数（字典dict）
    '''可变参数'''
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

'''数据容器'''
# 列表 list []：可修改 有序 元素重复
lst = [1, 2, 3]
# 元组 tuple ()：不可修改 有序 元素重复
tup = (1, 2, 3)
# 字典 dict {}：可修改 无序 键唯一
dct = {'key1': 'value1', 'key2': 'value2'}
# 集合 set {}：可修改 无序 元素唯一
st = {1, 2, 3}
# 字符串 str ""：不可修改 有序 元素重复
strg = "hello"

'''列表'''
A = List.index(value)#索引
A = List.count(value)#计数
List.append(value)#添加末尾
List.insert(index, value)#插入
List.remove(value)#删除第一个匹配项
List.delete(value)#删除指定元素
List.count(value)#计数
List.pop(index)#删除并返回指定索引元素，默认最后一个
List.sort()#排序
#ASCII 码排序
List.sort(reverse=True)#降序排序
List_1 = sorted(List, reverse=True)#返回排序后的新列表
List.sort(key=lambda x: x[1] / len)#按指定键排序


List.reverse()#反转
List.extend(iterable)#扩展列表 iterable = {1,2} / [1,2] / (1,2)
List.clear()#清空列表
List.copy()#浅拷贝,伴随改变
List + List #连接
List * n #重复
List[i:j:k]#切片
# i:开始索引 j:结束索引 k:步长
List[i] / List[-i]#索引访问 i:正向索引(0 -> n-1) -i:反向索引(-n -> -1)
len(List)#长度
min(List)#最小值
max(List)#最大值
sum(List)#求和
sorted(List)#返回排序后的新列表
reversed(List)#返回反转后的迭代器
list(range(5))#[0,1,2,3,4]
# range(start, end, step)
list("hello")#['h', 'e', 'l', 'l', 'o']

'''元组'''
tup = (1, 2, 3)
tup.index(value)#索引
tup.count(value)#计数
len(tup)#长度
min(tup)#最小值
max(tup)#最大值
sum(tup)#求和
tuple(iterable)#转换为元组
list(tup)#转换为列表
str(tup)#转换为字符串
sorted(tup)#返回排序后的新列表
reversed(tup)#返回反转后的迭代器
tuple(range(5))#(0,1,2,3,4)
# range(start, end, step)
tuple("hello")#('h', 'e', 'l', 'l', 'o')

'''字典'''
dct = {'key1': 'value1', 'key2': 'value2'}
dct.keys()#键视图
dct.values()#值视图
dct.items()#键值对视图
dct.get(key, default=None)#获取值
dct.update(other_dict)#更新字典
dct.pop(key, default=None)#删除并返回键对应的值
dct.popitem()#删除并返回最后一个键值对
dct.clear()#清空字典
dct.copy()#浅拷贝
len(dct)#长度
del dct[key]#删除键值对
key in dct#检查键是否存在
dict(iterable)#转换为字典
dict.fromkeys(keys, value=None)#创建新字典
dict(a=1, b=2)#创建字典

{'a': 1, 'b': 2}#创建字典
dct1 = {'a': 1}
dct2 = {'b': 2}
dct3 = {**dct1, **dct2}#合并字典

'''集合'''
st = {1, 2, 3}
st.add(value)#添加元素
st.remove(value)#删除元素，元素不存在时抛出 KeyError
st.discard(value)#删除元素，元素不存在时不抛出错误
st.pop()#删除并返回一个任意元素
