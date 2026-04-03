"""
字典的定义：使用{}，存储的元素是一个个的键值对
定义字典字面量：{key: value, key: value, ...}
定义字典字面量： my_dict = {key: value, key: value, ...}
定义空字典： my_dict = {}  my_dict = dict()
1. 字典和集合一样，不可以使用下标索引，但是字典可以通过key来获得对应的value
2. 字典的嵌套：字典的key和value可以是任意的数据类型（key不可以为字典），那就表明字典是可以嵌套的
"""

my_dict = {"ma": 99, "lu": 88, "liu": 77}
my_dict1 = {}
print(my_dict, my_dict1)
print(my_dict["ma"])
print(my_dict["lu"])
print(my_dict["liu"])
my_dict1 = {"ma": {"语文": 100, "数学": 100, "英语": 100}, "lu": {"语文": 90, "数学": 90, "英语": 90}, "liu": {"语文": 70, "数学": 70, "英语": 70}}
print(my_dict1)
print(my_dict1["ma"])
print(my_dict1["liu"])
print(my_dict1["ma"]["英语"])

"""
常用操作：
1. 新增（修改）
   语法：字典[key]= value，结果是字典被修改并且新增了元素
   语法：字典[key]= value，结果是字典被修改并且更新了元素
   （字典key不可以重复，所以对已存在的key执行上述操作，就是更新value值）
2. 删除
   语法：字典.pop(key)，结果就是获得指定key的value，同时字典被修改，指定的key的数据被删除
3. 获取全部的key（可以用来遍历字典）
   语法：字典.keys()，结果是得到字典中全部的key
"""
my_dict2 = {"wang": 90, "wu": 80}
my_dict2["wang"] = 70
print(my_dict2)
my_dict2["guo"] = 100
print(my_dict2)
my_dict2.pop("guo")
print(my_dict2)
keys = my_dict2.keys()
print(keys)
for key in keys:
    print(key)
for key in my_dict2:
    print(key)
# 以上两种遍历方式效果一样
len = len(my_dict2)
print(len)
my_dict2.clear()
print(my_dict2)
