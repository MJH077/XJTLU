"""
函数是组织好的且可以重复使用的用来实现特定功能的代码段
函数的定义：
def 函数名(传入参数)：
    函数体
    return 返回值
函数的调用：
函数名(参数)
（先定义函数后调用函数，参数和返回值不需要的时候可以省略不写）
"""
# 定义一个函数
def say_hi():
    print("我是小马")
# 调用函数,让定义的函数开始工作

if __name__ == '__main__':
    say_hi()


"""
x与y称为形式参数（形参），键盘输入的数据称为实际参数（实参）
传入参数的时候要和形式参数一一对应，参数按照顺序使用逗号分隔
传入参数的数量是不受限制的，可以不使用也可以有任意个
"""
def add(x, y):
    result = x + y
    print(f"结果为{result}")
add(int(input()), int(input()))


# 给函数添加说明文档，辅助理解函数的作用,以下为语法
# def fun(x, y):
#    """
#    函数说明
#    :param x:  形参x的说明
#    :param y:  形参y的说明
#    :return:   返回值的说明
#    """
#    函数体
#    return 返回值
def say_hi(a, b):
    """
    say_hi函数可以接收2个参数，进行2个数相加的功能
    :param a: 形参a表示相加的其中一个数字
    :param b: 形参b表示相加的另一个数字
    :return:  返回值是两数相加的结果
    """
    result = a + b
    return result
final1 = say_hi(1,2)
print(f"结果为{final1}")


# 函数的嵌套调用：指的是一个函数里面又调用了一个函数
def func_b():
    print("---2---")
def func_a():
    print("---1---")
    func_b()
    print("---3---")
func_a()

