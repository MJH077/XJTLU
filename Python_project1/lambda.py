"""
函数的定义中：
  def关键字，可以定义带有名称的函数（有名称的函数可以基于名称重复使用）
  lambda关键字，可以定义匿名函数（无名称）（无名称的匿名函数，只可以临时使用一次）
匿名函数定义语法：
  lambda 传入参数：函数体（一行代码）
  lambda是关键字，表示定义匿名函数
  传入参数表示匿名函数的形式参数，如x，y表示接收两个形式参数
  函数体就是函数的执行逻辑，要注意只能写一行，无法书写多行代码
"""

def test_func(computer):
    result = computer(1, 2)
    print(result)
test_func(lambda x, y: x + y)
test_func(lambda x, y: x + y)