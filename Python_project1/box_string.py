# 字符串是字符的容器，一个字符串可以存放任意数量的字符
# 和其他容器一样，字符串也可以通过下标索引进行访问，从前向后从0开始，从后向前从-1开始
# 同元组一样，字符串是一个无法修改的数据容器
"""
1.只可以存储字符串
2.长度任意，取决于内存大小
3.支持下标索引
4.允许重复字符出现
5.不可以修改
6.支持for循环

"""
my_str = "xiaoma"
value = my_str[0]
value1 = my_str[-2]
print(value, value1)
my_str1 = "xiao ma"

"""
1.查找特定字符串的下表索引值
  语法：字符串名称.index(特定字符串)
2.将字符串1的全部内容替换为字符串2（不是修改字符串本身，而是得到了一个新的字符串）
  语法：字符串名称.replace(字符串1, 字符串2)
3.字符串的分割，按照指定的分割字符串，将字符串划分为多个字符串，并存入列表对象中（字符串本身不变，而是得到了一个列表对象）
  语法：字符串.split(分割字符串)
4.字符串的规整操作，即去除前后空格   语法：字符串.strip()
  去除前后指定的字符串  语法：字符串.strip(字符串)
"""
value2 = my_str.index("ma")
print(value2)
new_str = my_str.replace("ma", "lu")
print(my_str, new_str)
my_str = "hello python"
new_str = my_str.split("e")
print(my_str, type(my_str), new_str, type(new_str))
my_str = " python "
new_str = my_str.strip()
print(my_str, new_str)
my_str = "12python21"
new_str = my_str.strip("12")
print(my_str, new_str)
my_str = "xiao ma and xiao lu"
num = my_str.count("xiao")
print(num)
count = len(my_str)
print(count)

