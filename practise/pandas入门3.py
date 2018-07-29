from pandas import Series, DataFrame, Index
import numpy as np

# 层次化索引  对数据重塑和分组操作很有用
data = Series(np.random.randn(10), index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                                          [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data)
print(data.index)
print(data['b'])
print(data['b':'c'])
print(data.ix[['b', 'd']])
print(data[:, 2])
print(data.unstack())  # 被安排进新的DataFrame中
print(data.unstack().stack())  # 上面的逆运算

frame = DataFrame(np.arange(12).reshape(4, 3), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['ohio', 'ohio', 'col'], ['green', 'red', 'green']])
print(frame)
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame)
print(frame['ohio'])

# 从新分级排序
print(frame.swaplevel('key1', 'key2'))  # 返回的是互换级别的新对象
print(frame.sortlevel(1))  # 对单个的值进行排序
print(frame.swaplevel(0, 1).sortlevel(0))

# 根据级别汇总统计
print(frame)
print(frame.sum(level='key2'))  # key2中相同的索引相加
print(frame.sum(level='color', axis=1))  # color相同的相加

# 使用DataFrame的列
frame = DataFrame({'a': range(7), 'b': range(7, 0, -1), 'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd': [0, 1, 2, 0, 1, 2, 3]})
print(frame)
print(frame.set_index(['c', 'd']))  # 选取其中的列变为行索引
print(frame.set_index(['c', 'd'], drop=False))  # 默认会移除，但是也可以保留下来
print(frame.set_index(['c', 'd']).reset_index())  # 是上上的反操作，把索引移到列里面

# 其他有关pandas的话题
# 整数索引
ser = Series(np.arange(3.))
# print(ser[-1])  # 整数索引和列表不一样， 这里会报错
print(ser)
ser2 = Series(np.arange(3), index=['a', 'b', 'c'])
print(ser2[-1])  # 非整数索引没有这样的歧义
print(ser.ix[:1])

ser3 = Series(range(3), index=[-5, 1, 3])
print(ser3)
# print(ser3.iget_value(2))  # 没有这个属性
frame = DataFrame(np.arange(6).reshape(3, 2), index=[2, 0, 1])
print(frame)
# print(frame.irow(0))
# print(frame.icol())

# pandas入门完结




