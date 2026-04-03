"""
文件的编码：
 编码技术就是翻译的规则，记录了如何将内容翻译成为二进制，以及如何将二进制翻译回可识别内容
 不同的编码，将内容翻译成二进制也是不同的（计算机中的可用编码：UTF-8，GBK,Big5等）
文件的操作：
  操作系统以文件为单位来管理磁盘中的数据，一般来说文件可以分为文本文件、视频文件、音频文件、图像文件、可执行文件等多种类别。
  在python中，使用open函数可以打开一个已经存在的文件或者创建一个新文件，语法为open(name, mode, encoding)
  1. name: 是要打开的目标文件名的字符串（可以包含文件所在的具体路径）
  2. mode： 设置打开文件的模式（访问模式）：只读、写入、追加等
     r：以只读方式打开文件，文件的指针将会放在文件的开头，这是默认模式
     w：打开一个文件只用于写入，如果该文件已存在则打开文件并从开头开始编辑，原有内容被删除；如果该文件不存在，则创建新文件
     a：打开一个文件用于追加，如果该文件已经存在，则新的内容将会被写入到已有内容之后；如果该文件不存在，则创建新文件后进行写入
  3. encoding: 编码格式（推荐使用UTF-8）
"""

"""
read()方法：
  语法：文件对象.read(num) num表示要从文件中读取数据的长度（单位在是字节），如果没有传入num，那么就表示读取文件中所有的数据
readlines()方法：
  readlines方法可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中的每一行数据为一个元素
（注意要在同级的情况下读取）
readline()方法：
  一次读取一行内容
"""
f = open("file测试.txt", "r", encoding="UTF-8")
print(f, type(f))
# encoding的顺序不是第三位，所以不能够用位置参数，用关键字参数直接指定
# f是open函数的文件对象
file1 = f.read(12)
file = f.read()
print(file1, file, type(file1), type(file))
# 当进行两次读取时，第二次读取会从第一次读取的结尾开始读取
# read()方法返回的是str类型
file2 = f.readlines()
print(file2, type(file2))
# 读取到的内容为空，因为调用读取对象之后，指针已经到达了最后一个字符，再往后读就为空了
# readlines()方法返回的是list类型
g = open("jack.txt", "r", encoding="UTF-8")
file3 = g.readlines()
print(file3)
h = open("jack1.txt", "r", encoding="UTF-8")
line1 = h.readline()
line2 = h.readline()
print(line1, line2)
print(type(line1), type(line2))
for x in h:
    print(x)

"""
关闭文件对象：
  语法为 文件对象.close()
  最后通过close来关闭文件对象，也就是关闭对于文件的占用
  如果不调用close，同时程序没有停止运行，那么这个文件就将一直被python占用
"""
f.close()
g.close()
h.close()

"""
with open语法：
with open(, , )as f:
通过在with open的语句块中对文件进行操作
可以在操作完成后自动关闭close文件，避免遗忘掉close方法
"""
with open("file测试.txt", "r", encoding="UTF-8")as f:
    file4 = f.read()
    print(file4)

"""
写入操作：
  1.打开文件：open
  2.文件写入：.write("内容")
  3.内容刷新： .flush()
直接调用write的话，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区
当调用flush的时候，内容会真正写入文件。这样做的目的是为了避免频繁的操作硬盘，导致效率下降
"""
x = open("jack2.txt", "w", encoding="UTF-8")
x.write("Hello,world!")
x.flush()
# 可以不写flush方法而直接调用close方法，因为close方法中已经内置了flush的功能
y = open("jack.txt", "a", encoding="UTF-8")
y.write("wangfeng")
y.close()
