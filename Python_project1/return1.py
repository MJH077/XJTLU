"""
如果一个函数写了两个return值，那么调用该函数只会执行第一个return，原因是return可以退出当前函数，导致return下方的代码不执行
如果一个函数需要拥有多个返回值，则可以通过逗号将返回值分隔开，按照返回值的顺序用多个变量来接收
牢记变量之间用逗号隔开，并支持不同类型的数据进行return
"""

def test_return():
    return 1, "Hello", True
x, y, z = test_return()
print(x)
print(y)
print(z)