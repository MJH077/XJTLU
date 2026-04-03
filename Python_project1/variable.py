"""
变量作用域指的是变量的作用范围（在哪里可以使用，在哪里不可以使用）
主要分为：全局变量与局部变量
局部变量即定义在函数体内部的变量，只在函数体内部生效。作用是可以在函数体内部临时保存数据，完成后销毁局部变量
全局变量即在函数体内和外都生效的变量
"""
def test_a():
    num = 100
    print(num)
test_a()

num = 100
def test_a():
    print(f"test_a为{num}")
def test_b():
    print(f"test_b为{num}")
test_a()
test_b()
print(num)

# 使用global关键字，可以在函数内部声明变量为全局变量
num = 100
def test_a():
    print(f"test_a为{num}")
def test_b():
    global num
    num = 500
    print(f"test_b为{num}")
test_a()
test_b()
print(num)
