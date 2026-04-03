"""
捕获异常的作用在于：提前假设某处会出现异常，做好提前的准备，当真的出现异常的时候，可以有后续手段
语法：
  try:可能发生错误的代码
  except：如果出现异常执行的情况
"""
try:
    f = open("abc.txt", "r", encoding="UTF-8")
except:
    print("出现异常，用w模式打开")
    f = open("abc.txt", "w", encoding="UTF-8")

"""
捕获指定的异常：
try: print(name)
except NameError as e: print("name变量名称未定义错误")
1. 如果尝试执行的代码的异常类型和要捕获的异常类型不一样，则无法捕获异常
2. 一般try的下方只放一行尝试执行的代码
"""
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的现象")
    print(e) # e是异常的具体信息

"""
捕获多个异常：当捕获了多个异常的时候，可以把要捕获的异常类型的名字放在except之后，并且使用元组的方式进行书写
try: print(1/0)
except(NameError, ZeroDivisionError): print("出现了...的异常")
"""
try:
    print(1/0)
except(NameError, ZeroDivisionError)as e:
    print("出现了变量未定义或者除数为零的异常")
    print(e)

"""
捕获所有的异常（try/except也可以）：
try:
except Exception as e:
"""
try:
    f = open("efg.txt", "r", encoding="UTF-8")

except Exception as e:
    print("出现异常了")
    print(e)

try:
    print(1/1)
except:
    print("出现异常")
else:
    print("没有出现异常")
# else作为没有异常发生时执行的代码

try:
    f = open("123.txt", "r", encoding="UTF-8")
except Exception as e:
    print("出现异常")
    f = open("123.txt", "w", encoding="UTF-8")
else:
    print("没有异常")
finally:
    f.close()
# finally表示有没有异常都要执行

"""
异常具有传递性：
当函数func01中发生异常，并且没有捕获处理这个异常的时候，异常会被传递到函数func02，当func02也没有捕获处理这个异常的时候，main含捕获这个异常
这就是异常的传递性（当所有函数都没有捕获异常的时候，程序就会报错）
"""
def func01():
    print("func01 begin")
    num = 1/0
    print("func01 over")
def func02():
    print("func02 begin")
    func01()
    print("func02 over")
def main():
    try:func02()
    except Exception as e:
        print(e)
main() 




