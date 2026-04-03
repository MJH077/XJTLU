"""
 位置参数：调用函数的时候根据函数定义的参数位置来传递参数，传递的参数和定义的参数的顺序及个数必须一致
"""
def user_info(name, age, gender):
    print(f"您的名字是{name}，年龄是{age}，性别是{gender}")
user_info("Tom", 29, "男")

"""
 关键字参数：函数调用时通过“键=值”形式传递参数，可以让函数更加清晰且容易使用，同时也清除了参数的顺序要求
 关键字参数可以和位置参数混用，但是位置参数必须在前，且要匹配参数顺序
"""
def user_info1(name, age, gender):
    print(f"您的名字是{name}，年龄是{age}，性别是{gender}")
user_info1(name = "jack", age = 20, gender = "男")
user_info1("Leo", age = 30, gender = "男")

"""
 缺省参数：也叫做默认参数，用于定义函数，为参数提供默认值，调用函数时可以不传该默认参数的值（所有位置参数必须出现在默认参数之前，包括函数定义和调用）
 当调用函数时没有传递参数，就会使用默认是用缺省参数对应的值
"""
def user_info2(name, age, gender = "男"):
    print(f"您的名字是{name}，年龄是{age}，性别是{gender}")
user_info2("peter", 20, "女")
user_info2("mam", 10)

"""
 不定长参数：也叫作可变参数，用于不确定调用的时候会传递多少个参数（不传递也可以）的场景
 当调用函数时不确定参数的个数时，可以使用不定长参数
 类型有：位置传递与关键字传递 
 1. 位置传递：传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元祖tuple，args是元
 祖类型，这就是位置传递
 2. 关键字传递：参数是“键=值”形式的形式情况下，所有的“键=值”都会被kwargs接收，同时组成字典
"""
def user_info3(*args):
    print(args)
user_info3("kobe", 20, "男", "IMIS")
def user_info4(**kwargs):
    print(kwargs)
user_info4(name = "james", age = 20, gender = "男")