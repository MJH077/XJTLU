"""
数据容器的通用操作：
1. 遍历
   五种数据容器都支持for循环遍历，集合和字典不支持while循环遍历（无法下标索引），其他都支持
2. 统计功能
    len(容器) 统计容器的元素个数
    max(容器) 统计容器的最大元素
    min(容器) 统计容器的最小元素
"""
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_str = "123"
my_set = {1, 2, 3}
my_dict = {"1": 1, "2": 2, "3": 3}
print(len(my_list))
print(max(my_list))
print(min(my_list))
print(len(my_str))
print(max(my_str))
print(min(my_str))
print(len(my_tuple))
print(max(my_tuple))
print(min(my_tuple))
print(len(my_set))
print(max(my_set))
print(min(my_set))
print(len(my_dict))
print(max(my_dict))
print(min(my_dict))

"""
容器的类型转换
"""
print(list(my_list))
print(list(my_tuple))
print(list(my_set))
print(list(my_dict))
print(list(my_str))
print(tuple(my_list))
print(tuple(my_tuple))
print(tuple(my_set))
print(tuple(my_dict))
print(tuple(my_str))
print(str(my_list))
print(str(my_tuple))
print(str(my_set))
print(str(my_dict))
print(str(my_str))
print(set(my_list))
print(set(my_tuple))
print(set(my_set))
print(set(my_dict))
print(set(my_str))

"""
容器的排序功能：
sorted(容器, [reverse = True]), 将给定容器进行排序
[reverse = True] 意味着将排序结果反转
"""
result = sorted(my_list)
result1 = sorted(my_tuple)
result2 = sorted(my_set)
result3 = sorted(my_dict)
result4 = sorted(my_str)
print(result)
print(result1)
print(result2)
print(result3)
print(result4)
result = sorted(my_list, reverse=True)
result1 = sorted(my_tuple, reverse=True)
result2 = sorted(my_set, reverse=True)
result3 = sorted(my_dict, reverse=True)
result4 = sorted(my_str, reverse=True)
print(result)
print(result1)
print(result2)
print(result3)
print(result4)




