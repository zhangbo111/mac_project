import pandas as pd
import numpy as np
# 自动创建索引
obj = pd.Series([4, 7, -5, 2])
print(obj, type(obj))
print(obj.values)
print(obj.index)

# 自己创建索引
obj2 = pd.Series([2, 5, -32, 3], index=['a', 'b', 'c', 'd'])
print(obj2)
print(obj2['a'])  # 通过索引拿取值
print(obj2[['a', 'c']])

# 数组运算
print(obj2[obj2 > 0])
print(obj2 * 2)
print('b' in obj2)

# 可以通过字典来创建Series
sdata = {'zhangbo': 110, 'zhangwu': 150}
obj3 = pd.Series(sdata)
print(obj3)
# 自动找到对应的索引
states = ['zhangwu', 'zhangbo', 'zhangkai']
obj4 = pd.Series(sdata, index=states)
print(obj4)
print(pd.isnull(obj4))
print(pd.notnull(obj4))
print(obj4.isnull())
print(obj3 + obj4)

# name属性
obj4.name = 'sea'
obj4.index.name = 'state'
print(obj4)

# 索引通过赋值方式进行修改
obj.index = ['bob', 'steve', 'jeff', 'ryan']
print(obj)

# DataFrame第二种pandas中的数据类型，表格型数据结构，数据框
# 既有行索引，又有列索引
data = {
    'state': ['ohio', 'ohio', 'ohio', 'nevada', 'nevada'],
    'year': [2000, 2001, 2002, 2001, 2002],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
}
# 自动创建索引 0 - N-1
frame = pd.DataFrame(data)
print(frame)
# 按指定列进行排列
frame = pd.DataFrame(data, columns=['year', 'state', 'pop'])
print(frame)

# 传入的列找不到数据，则产生NA值, 可以自己创建索引
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
print(frame2)
print(frame2.columns)  # 单独打印列的名称
print(frame2['state'])  # 获取列
print(frame2.ix['two'])  # 获取行
frame2['debt'] = 16.5  # 修改列的值
frame2['debt'] = np.arange(5)   # 自增
print(frame2)
# 列表或者数组赋值给列, Series精确匹配
val = pd.Series([-23, 3, -4], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)
# 为不存在的列赋值会创造一个新列
frame2['eastern'] = frame2.state == 'ohio'
print(frame2)
del frame2['eastern']  # 关键字del用于删除列
print(frame2)

# 嵌套字典（字典的字典）
pop = {
    'nevada': {
        2001: 2.4,
        2002: 2.9
    },
    'ohio': {
        2000: 1.5,
        2001: 1.7,
        2002: 3.6
    }
}
frame3 = pd.DataFrame(pop)
print(frame3)  # 内层的键会合并形成最终的索引，如果指定索引，则不会这样
print(frame3.T)  # 进行转置
frame3 = pd.DataFrame(pop, index=[2001, 2002, 2003])  # 如果指定索引，则不会这样
print(frame3)
# data数据类型是可以切割的
pdata = {
    'ohio': frame3['ohio'][:-1],
    'nevada': frame3['nevada'][:2]
}
frame4 = pd.DataFrame(pdata)
print(frame4)
# 设置index和columns的name属性,这些信息也会被显现出来
frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)
print(frame3.values)  # 单独获取值
print(frame2.values)
