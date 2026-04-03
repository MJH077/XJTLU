"""
 函数作为参数传递：
   test_func需要一个函数作为参数传入，这个参数需要接受两个数字进行计算，计算逻辑由这个被传入函数决定
   computer函数接收两个数字对其进行计算，computer函数作为参数，传递给了test_func函数使用
   最终在test_func函数的内部，由传入的computer函数完成对数字的计算操作
(函数传入的作用在于：传入计算逻辑，而非传入数据)
"""
def test_func(computer):
    result = computer(int(input()), int(input()))
    print(result)
    print(type(computer))
def computer(x, y):
    return x+y
test_func(computer)

