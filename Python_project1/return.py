"""
所谓返回值，就是在程序当中函数完成事情之后，最后给调用者的结果
返回值语法：
def 函数(参数)：
    函数体
    return 返回值
变量 = 函数(参数)
（用变量来接收返回值，函数体遇到return就结束了，所以写在return后的代码不会执行）
"""
def add(a,b):
    result = a + b
    return result
r = add(5, 6)
print(r)


"""
无返回值的函数，实际上是返回了None这个字面量
None的类型是<class 'NoneType'>
None的意思是空的意思，没有什么实际意义
"""
def say_hi():
    print()
result = say_hi()
print(f"返回的内容为{result}")
print(f"返回的内容类型为{type(result)}")
def say_hi1():
    print()
    return None
result = say_hi1()
print(f"返回的内容为{result}")
print(f"返回的内容类型为{type(result)}")