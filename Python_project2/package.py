"""
面向对象编程是基于模板（类）去创建实体（对象），使用对象完成功能开发
三大特性：封装、继承、多态
"""
import json

"""
封装：封装表示的是将现实世界的属性和行为，封装到类中并描述为成员变量和成员方法
私有成员：既然现实世界又不考公开的属性和行为，那么作为现实事物在程序中映射的类也应该支持
类中提供了私有成员变量和私有成员方法的形式来支持
定义方法：
1. 私有成员变量：变量名以__开头
2. 私有成员方法：方法名以__开头
注意：私有的变量和方法只能够类的内部进行使用，即类对象无法访问私有成员，但类中的其他成员可以访问私有成员
意义：在类中提供仅供内部使用的属性和方法而不对外开放
"""
class Phone:
    __current_voltage = 0.5
    def __keep(self):
        print("keep cpu single core")
    def call(self):
        if self.__current_voltage >= 1:
            print("ok")
        else:
            self.__keep()
            print("ok")
phone = Phone()
phone.call()
# phone.__keep()
# print(phone.__current_voltage)

"""
继承： class 类名(父类名)：类内容体
"""
# 单继承
class Phone1:
    fourG = None
    produce = 'i'
    def call_by_4G(self):
        print("4G通话")
class Phone2(Phone1):
    face_id = '10010'
    def call_by_5G(self):
        print("5G通话")
phone = Phone2()
print(phone.produce)
phone.call_by_5G()
phone.call_by_4G()
# 多继承：一个类可以继承多个父类（多继承中，如果父类有同名方法或者属性，先继承的优先级高于后继承的）
class nfcreader:
    nfc_type = "5"
    producer = 'h'
    def read_card(self):
        print("读卡")
    def write_card(self):
        print("写卡")
class remotecontorl:
    rc_type = "红外"
    def contorl(self):
        print("红外遥控开启")
class Myphone(Phone2, nfcreader, remotecontorl):
    pass  # pass是占位语句，用来保证函数（方法）或类定义的完整性，表示无内容、空的意思
phone13 = Myphone()
phone13.call_by_4G()
phone13.read_card()
phone13.write_card()
phone13.contorl()

"""
父类的复写：子类继承父类的成员属性和成员方法之后，如果对其不满意的话可以进行复写（在子类当中重新定义同名的属性或方法即可）
调用父类同名成员：一旦复写父类成员，那么类对象调用成员的时候，就会调用复写后的新成员。如果需要使用被复写的父类成员，需要使用特殊的调用方式
1. 使用成员变量：父类名.成员变量 
   使用成员方法：父类名.父类方法(self)
2. 使用成员变量：super().成员变量
   使用成员方法：super().成员方法()
"""
class Myphone1(Phone2, nfcreader, remotecontorl):
    producer = "p"
    def pro(self):
        print(super().producer)
phone14 = Myphone1()
print(phone14.producer)
phone14.pro()

"""
类型注解：在代码涉及数据交互的地方，提供数据类型的注解（显示的说明）
主要功能：帮助第三方IDE工具（如pycharm）对代码进行类型判断，协助做代码提示；帮助开发者自身对变量进行类型注释
语法：变量：类型 
注意：注释类型只是提示型的，并不会真正的对类型做出验证和判断，不相符不会报错
"""
# 基础数据的类型注释
var_1: int = 10
var_2: str = "jack"
var_3: bool = True
# 类对象类型注释
class Student:
    pass
stu: Student = Student()
# 基础容器类型注释
my_list: list = [1, 2]
my_tuple: tuple = (1, 2)
my_dict: dict = {"jack": 20}
# 容器类型注释
my_list1: list[int] = [1, 2]
my_tuple1: tuple[int, str, bool] = (10, "leo", True)
my_dict1: dict[str, int] = {"jack": 20}
# 注释中的类型注解（语法：# type:类型）
var_4 = json.loads('{"name": "lucy"}')   # type: dict[str, str]

"""
函数和方法的形参类型注解语法：
def 函数方法名(形参名：类型, 形参名：类型, ...)
    pass
"""
def add(x: int, y: int):
    return x + y
# 对返回值进行注解
def func(data: list) -> list:
    return data
# union类型注解
from typing import Union
my_list: list[Union[int, str]] = [1, 2, "str"]
def func(data: Union[int, str]) -> Union[int, str]:
    pass

"""
多态：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态
多态常运用在继承关系上，比如函数（方法）形参声明接收父类对象，实际是传入父类的子类对象进行工作
以父类做声明，以子类做实际工作，用以获得同一行为但不同状态
"""
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")
def make_noise(animal: Animal):
    animal.speak()
dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)

"""
抽象类（接口）：父类来确定有哪些方法，具体的方法实现由子类自行决定
抽象类：含有抽象方法的类称之为抽象类
抽象方法：方法体是空实现的（pass）称之为抽象方法
"""
class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l(self):
        pass
class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")
    def hot_wind(self):
        print("美的空调制热")
    def swing_l(self):
        print("美的空调摆风")
class Gree_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")
    def hot_wind(self):
        print("格力空调制热")
    def swing_l(self):
        print("格力空调摆风")
def make_cool(ac: AC):
    ac.cool_wind()
def make_hot(ac: AC):
    ac.hot_wind()
def make_swing(ac: AC):
    ac.swing_l()
midea_ac = Midea_AC()
gree_ac = Gree_AC()
make_cool(midea_ac)
make_cool(gree_ac)
make_hot(midea_ac)
make_hot(gree_ac)
make_swing(midea_ac)
make_swing(gree_ac)






