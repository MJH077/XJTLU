# 类和对象
"""
使用类去封装属性，并基于类创建出一个个的对象来使用
类的使用语法：
class 类名称：类的属性 类的行为
（class是关键字，表示要定义类了；类的属性就是定义在类中的变量-成员变量；类的行为就是定义在类中的函数-成员方法）
创建类对象的语法：
对象=类名称()
成员方法的定义语法：
def 方法名(self, 形参1, ..., 形参n)：方法体
self关键字是成员方法定义的时候必须填写的，它用来表示类对象自身的意思
当我们使用类对象调用方法时self会自动被python传入
在方法内部，想要访问类的成员变量就必须使用self
"""
class Student:
    name = None
    gender = None
    nationality = None
    age = None
stu = Student()
stu.name = "jack"
stu.gender = "男"
stu.nationality = "广西"
stu.age = 20
print(stu)

class Student:
    name = None
    def say_hi(self):
        print(f"Hello, 我是{self.name}")
    def say_hi2(self, msg):
        print(f"Hello, 我是{self.name}, {msg}")
stu = Student()
stu.name = "jack"
stu.say_hi()
stu.say_hi2("你好")

"""
面向对象: 使用对象进行编程，使用对象来完成具体的工作
"""
class Clock:
    id = None
    price = None
    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)
clock = Clock()
clock.id = "003032"
clock.price = 20
print(f"闹铃ID为{clock.id},价格为{clock.price}")
clock.ring()

"""
方法
构造方法: __init__()称为构造方法
  在创建类对象（构造类）的时候，会自动执行
  在创建类对象（构造类）的时候，将传入参数自动传递给__init__方法使用 
"""
class Student1:
    name = None
    age = None
    tel = None
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
stu1 = Student1("leo", 20, 1300000000)
print(stu1.name)
print(stu1.age)
print(stu1.tel)

"""
魔术方法：
__init__构造方法
__str__字符串方法
__lt__小于、大于符号比较
__le__小于等于、大于等于符号比较
__eq__==符号比较
"""
class Student2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student2: name is {self.name}, age is {self.age}"
    def __lt__(self, other):
        return self.age < other.age
    def __le__(self, other):
        return self.age < other.age
    def __eq__(self, other):
        return self.age < other.age
stu2 = Student2("lucy", 30)
stu3 = Student2("jack", 90)
stu4 = Student2("lucy", 30)
stu5 = Student2("jack", 30)
print(stu2)
print(str(stu2))
print(stu2 < stu3)
print(stu2 > stu3)
print(stu4 <= stu5)
print(stu4 >= stu5)
print(stu2 == stu3)



