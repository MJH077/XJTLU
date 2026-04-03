"""
python模块是一个python文件，以.py结尾。模块能够定义函数、类和变量，模块里也能够包含可执行的代码
模块的作用：可以认为一个模块就是一个工具包，没一个工具包都有各种不同的工具供我们使用进而实现各种不同的功能
模块的导入方式：[from 模块名] import [模块|类|变量|函数|*] [as 别名]
常见的组合形式：
  import 模块名
  from 模块名 import类、变量、方法等
  from 模块名 import *
  import 模块名 as 别名
  from 模块名 import 功能名 as 别名
"""

import time  # 导入python内置的time模块，ctrl+左键点击time可以查看该文件
print("hello")
time.sleep(2)  # 睡眠两秒（通过·就可以使用模块内部的全部功能）
print("world")

from time import sleep
print("hello")
sleep(2)  # 不需要·，可以直接使用sleep功能
print("world")

from time import *  # 与第一个的效用一致，但该写法不用加.功能名
print("hello")
sleep(2)  # 不需要·，可以直接使用sleep功能
print("world")

import time as t
print("hello")
t.sleep(2)
print("world")

from time import sleep as s
print("hello")
s(2)
print("world")

"""
自定义模块：新建一个python文件，命名为模块名，并定义函数
每一个python文件都可以作为一个模块，模块的名字就是文件的名字，也就是说自定义模块必须要符合标识符命名规则
"""
import function
function.say_hi()
# 如果在本模块中不写上一行代码，结果也仍然能够输出，因为在function模块中已经将该功能调用了
# 如果在function模块中添加main函数，在main函数中调用了该功能，那么在本模块中无论调不调用都不会输出结果了

"""
如果一个模块文件中有__all__变量，当使用from xxx import * 导入的时候，就只能导入这个列表之中的元素
连接function1
"""
from function1 import *
x(2,1)
# y(2, 1)不会被调用，当然手动调用y功能可以解决

"""
python包：从物理上来看，包就是一个文件夹，在该文件夹下包含了一个__init__.py文件，该文件夹可用于包含多个模块文件；从逻辑上来看，包的本质依然是模块
步骤：new、python package、输入包名、新建成功（新建包后，包内会自动创建__init__.py文件，这个文件控制着包的导入行为）
导入方式： import 包名.模块名
以下的代码也适用于__all__=[" "]的规则
"""
import my_package.my_module
my_package.my_module.jack()
from my_package import my_module
my_module.jack()
from my_package.my_module import jack
jack()

"""
第三方包：一个包，就是一堆同类型功能的集合体
如科学计算中的numpy包、数据分析中的pandas包、人工智能中的tensorflow包 
由于是第三方，所以python没有内置，这就需要我们安装它们才可以导入使用

安装第三方包：pip
打开dos在里面输入pip install 包名称，即可通过网络快速安装第三方包
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
"""


