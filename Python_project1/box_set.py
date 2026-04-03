""
定义集合字面量：{元素，...}
定义集合变量：变量名称 = {元素，...}
定义空集合： 变量名称 = set()
"""

my_set = {"huren", "yongshi", "qishi", "duxingxia", "huren"}
my_set_empty = set()
print(f"my_set的内容是{my_set}，类型是{type(my_set)}；my_set_empty的内容是{my_set_empty}，类型是{type(my_set_empty)}")
# 集合会去重，且顺序得不到保障

"""
1. 添加：
    因为集合是无序的，所以集合不支持下标索引访问，但是和列表一样是允许修改的
    语法：集合.add(元素) 表示将指定元素添加到集合当中
2. 移除：
    语法：集合.remove(元素)  表示将指定元素从集合中去除
3. 随机取出：
    语法：集合.pop() 表示从集合中随机取出一个元素，同时集合本身被修改
4. 清空集合：
    语法：集合.clear()
5. 取出两个集合的差集
    语法：集合1.difference(集合2) 表示取出集合1和集合2的差集（集合1有而集合2没有的）
    结果是得到一个新集合，集合1和集合2不变
6. 消除两个集合的差集
    语法：集合1.difference_update(集合2)  表示在集合1内删除和集合2相同的元素
    结果是集合1被修改，集合2不变
7. 两个集合取并集
    语法：集合1.union(集合2)  将集合1和集合2组合成新集合，得到新集合后集合1和集合2不变
8. 集合的遍历：
    因为集合不支持下标索引，所以不用使用while循环，可以使用for循环
"""
my_set.add("maci")
my_set.add("maci")
print(f"新集合的结果为{my_set}")
my_set.remove("yongshi")
print(f"新集合的结果为{my_set}")
result = my_set.pop()
print(result)
result1 = my_set.clear()
print(result1)
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"取差集后为{set3}，原来的两个集合未变化{set1}和{set2}")
set4 = set1.difference_update(set2)
print(f"取差集后为{set4}，原来的两个集合变化{set1}和{set2}")
set5 = set1.union(set2)
print(f"取差集后为{set5}，原来的两个集合未变化{set1}和{set2}")
len = len(set5)
print(len)
for element in set5:
    print(f"集合中的元素有{element}")