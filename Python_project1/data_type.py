# 通过type()语句来验证得来数据的类型
print(type(7))
float_type = type(3.14)
print(float_type)
name = "Hello,World!"
name_type = type(name)
print(name_type)

"""
数据类型转换：
从文件中读取的数字默认是字符串，需要转换成数字类型
input()语句默认结果是字符串，若需要数字也要进行转换
将数字转换成字符串用以写出到外部系统等等
"""
num_str = str(7)
print(type(num_str), num_str)
float_str = str(3.14)
print(type(float_str), float_str)
num = int("11")
print(type(num), num)
num1 = float("3.14")
print(type(num1), num1)
float_num = float(7)
print(type(float_num), float_num)
int_num = int(3.14)
print(type(int_num), int_num)
# 并不是四舍五入取整，而是去尾法取整
