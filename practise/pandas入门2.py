from pandas import Series, DataFrame, Index
import numpy as np
obj = Series(range(3), index=['a', 'b', 'c'])
print(obj)
index = obj.index
print(index)
print(index[1:])
# index[1] = 'd'  index对象时不可以被修改的  为了安全和共享

index = Index(np.arange(3))
obj2 = Series([1.5, -2.6, 0], index=index)
print(obj2.index is index)
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
frame3 = DataFrame(pop)
frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)
print('ohio' in frame3.columns)
print(2003 in frame3.index)  # index有很多的方法和属性（有时间呢，可以摸索一下）

# reindex创建适应新索引的新对象（这里我不是很懂）
obj = Series([2.3, 4.5, -23.3, 4.3], index=['d', 'b', 'a', 'c'])
print(obj)
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)  # 索引和值一一对应，根据新索引进行重排
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
print(obj2)  # 索引不存在，可以引入缺失值

obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
# obj3 = obj3.reindex(range(6), method='ffill')  # 或者pad
# print(obj3)  # 向前值填充
obj3 = obj3.reindex(range(6), method='bfill')  # 或者pad
print(obj3)  # 向后值填充



