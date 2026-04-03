"""
元组同列表一样，都是可以封装多个且可以是不同类型的元素在内，但是最大的不同点在于元组一旦定义完成就不可以被修改
定义元组变量：变量名称=(元素，元素，元素...)
定义空元组：变量名称=() 变量名称=tuple()
如果只有单个元素，那么必须加上逗号，否则就不是元组了
"""
t1 = (1, 2, 3, 4)
print(t1)
t2 = ("hello")
t3 = ("hello",)
print(type(t2))
print(type(t3))
t4 = ((1, 2, 3), (4, 5, 6))
print(type(t4))
print(t4[1][2])
index = t4.index((1, 2, 3))
print(index)
count = t4.count((1, 2, 3))
print(count)
num = len(t4)
print(num)

"""
元组里的内容不可以修改，修改了会直接发生报错
但是可以修改元组内list的内容
"""
t5 = ((1, 2, 3), [4, 5, 6])
print(t5)
t5[1][2] = 9
print(t5)