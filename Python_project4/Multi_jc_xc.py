"""
多任务：
1. 并发：在一段时间内交替去执行多个任务，例如对于单核CPU处理多任务时操作系统轮流让各个任务交替执行。
由于处理时间快，所以看上去是一起执行的。并发的任务数量大于CPU的核心数。
2. 并行：在一段时间内真正意义的同时一起执行多个任务。对于多核CPU处理多任务，操作系统会给CPU的每个内核安排一个执行的任务，
多个内核是真正的一起同时执行多个任务。并行的任务数量小于或等于CPU的核心数。

进程：是资源分配的最小单位，是操作系统进行资源分配和调度运行的基本单位。
即一个正在运行的程序就是一个进程，不在运行的就是程序。一个程序运行后至少有一个进程

多进程：
程序运行会默认创建一个进程，这个默认创建的进程称之为主进程；
在程序运行后又创建了一个进程叫做子进程

进程的创建步骤：
1. 导入进程包 import multiprocessing
2. 通过进程类创建对象 进程对象=multiprocessing.Process(target=任务名)
（target：执行的目标任务名，这里指的是函数名、方法名
  name：进程名，一般不用设置
  group：进程组，目前只能够使用None）
3. 启动进程执行任务 进程对象.start()
"""


"""
# 进程执行带有参数的任务 参数名：args（以元组的方式给执行任务传参）kwargs（以字典的方式给执行任务传参）
play_process = multiprocessing.Process(target=play, args=(3,))
do_process = multiprocessing.Process(target=do, kwargs={"num": 3})
"""

"""
获取进程编号的两种方式：
1.获取当前进程编号
os.getpid()
2.获取当前父进程编号
os.getppid()
通过比较当前进程和当前父进程的编号来确定方法是否是由主进程创建出来的
"""


import multiprocessing
import time
import os


def sing():
    for i in range(3):
        print("sing...")
        time.sleep(0.5)


def dance():
    for i in range(3):
        print("dance...")
        time.sleep(0.5)


def play(num, name):
    print("play进程pid编号：", os.getpid())
    for i in range(num):
        print(name)
        print("play...")
        time.sleep(0.5)


def do(num, name):
    print("do进程pid编号：", os.getpid())
    for i in range(num):
        print(name)
        print("do...")
        time.sleep(0.5)


def work():
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)


if __name__ == '__main__':
    # 使用进程类创建进程对象
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)
    play_process = multiprocessing.Process(target=play, args=(3, "小马"))
    do_process = multiprocessing.Process(target=do, kwargs={"num": 3, "name": "小马"})
    work_process = multiprocessing.Process(target=work)

    print("play进程的pid：", os.getpid())
    print("play进程的父进程pid：", os.getppid())
    print("do进程的pid：", os.getpid())
    print("do进程的父进程pid：", os.getppid())

    # 使用进程对象启动执行指定任务
    sing_process.start()
    dance_process.start()
    play_process.start()
    do_process.start()
    # 主进程不会立刻结束，会等待子进程全部结束才会结束。可以使用True来守护主进程，主进程退出之后子进程直接销毁，不再进行子进程中的代码（该例子为work）
    work_process.daemon = True
    work_process.start()
    time.sleep(1)
    print("主进程执行完成！")

"""
进程是分配资源的最小单位，一旦创建一个进程就会分配一定的资源。
线程是程序执行的最小单位，实际上进程只负责分配资源，而利用这些资源执行程序的是线程。
也就是说进程是线程的容器，一个进程中最少有一个线程来负责执行程序。
同时线程自己不拥有系统资源，只需要一点在运行中必不可少的资源，但是它可以与同属一个进程的其他线程共享进程所拥有的全部资源。
1. 导入线程模块 import threading
2. 通过线程类创建线程对象 线程对象=threading。Tread(target=任务名)
3. 启动线程执行任务 线程对象.start()
和进程的是十分类似的

线程之间的执行顺序是无序的，如果看到的执行顺序是有序的，只能说明电脑CPU很快
"""















