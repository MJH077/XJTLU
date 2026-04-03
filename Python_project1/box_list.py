# 数据容器：一种可以容纳多份数据的数据类型，容纳的每一份数据称之为一个元素，每一个元素可以是任意的数据类型，如字符串、布尔等等
# 列表list，元组tuple，字符串str，集合set，字典dict

"""
定义变量:
变量名称=[元素1，元素2...] （数据容器中的每一份数据都称之为元素）
定义空列表：
变量名称=[]
变量名称=list()
"""
name = ['xiaoma', 7, True]
print(name)
print(type(name))
name_list = [[1, 2, 3], [4, 5, 6]]
print(name_list)
print(type(name_list))

"""
1.列表中的每一个元素都有其位置下标索引，从前向后从0开始依次递增（也可以反向索引，从后往前从-1开始依次递减）
2.语法：列表[下标索引] （嵌套语法：列表[下标索引][下标索引]...） 通过下标索引取数据，超出取值范围会发生报错
3.可以容纳多个元素，上限为2**63-1
4.可以容纳不同类型的元素，是混装的
5.数据是有序储存的，拥有下标序号
6.允许数据重复出现，并且可以修改
"""
no_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(no_list[0])
print(no_list[1])
print(no_list[2])
print(no_list[-1])
print(no_list[-2])
print(no_list[-3])
print(no_list[0][2])
print(no_list[1][2])
print(no_list[2][2])

"""
函数是一个封装的代码单元，可以提供特定功能。如果将函数定义为class的成员，那么函数将会被称为方法
函数的使用：变量名=函数名(实参)  方法的使用：变量名1=类名() 变量名2=变量名1.方法名(实参)
1.列表的查询功能（方法）
  查找指定元素在列表的下标，如果找不到则报错
  语法：列表.index(元素)
2.列表的修改功能（方法）
  直接对指定下标（正向、反向下标均可）的值进行修改
  语法：列表[下标]=值
3.列表的修改功能（方法）--插入
  在指定的下标位置插入指定的元素
  语法：列表.insert(下标，元素)
4.列表的修改功能（方法）--追加
  将指定元素追加到列表的尾部
  语法：列表.append(元素)
5.列表的修改功能（方法）--追加一批数据
  将其他数据容器的内容取出并依次追加到列表的尾部
  语法：列表.extend(其他数据容器)
6.列表的修改功能（方法）--删除元素
  语法1：del 列表[下标]
  语法2：列表.pop(下标)
  语法3：列表.remove(元素)
7.列表的修改功能（方法）--清空列表
  语法：列表.clear()
8.统计某元素在列表中的数量
  语法：列表.count(元素)
9.统计列表中元素的数量
  语法:len(列表)
ton
  """
mylist = ['c', 'python', 'java']
index = mylist.index('java')
print(index)
print(type(index))
mylist[0] = 'c++'
print(mylist[0])
print(mylist.index('c++'))
mylist.insert(1, 'c')
print(mylist[1])
print(mylist)
mylist.append('rust')
print(mylist.index('rust'))
print(mylist)
mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(mylist[5])
print(mylist[6])
print(mylist[7])
del mylist[7]
print(mylist)
mylist.pop(6)
print(mylist)
mylist.remove(1)
print(mylist)
mylist.clear()
print(mylist)
mylist = [1, 1, 1, 2, 3, 4]
x = mylist.count(1)
print(x)
y = len(mylist)
print(y)

"""
列表的遍历：将容器内的元素依次取出进行处理的行为，称之为遍历、迭代（使用while,for循环遍历列表中的元素）
1.在循环控制上，while可以自定循环条件，for不可以自定循环条件且只能够一个个地从容器中取出数据
2.在无限循环上，while可以通过条件控制做到无限循环，for理论上不可以，因为遍历的容器变量不是无限的
3.在使用场景上，while适用于任何想要循环的场景，for适用于遍历数据容器的场景或者简单的固定次数循环场
"""
my_list = [1, 2, 3]
def list_while_func():
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(element)
        index += 1
def list_for_func():
    for num in my_list:
        print(num)
list_while_func()
list_for_func()


