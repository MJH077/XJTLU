# while的条件需要得到布尔类型，True表示继续循环，False表示结束循环
i = 0
while i < 10:
    print("无")
    i += 1
print("好")

# 1-100的和
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
    print(sum)

i = 1
while i <= 10:
    print(f"今天是第{i}天...")
    j = 1
    while j <= 10:
        print(f"送给她第{j}只玫瑰花")
        j += 1
    print("我喜欢你")
    i += 1
print(f"坚持到第{i-1}天，成功")

"""
九九乘法表
1.输出不换行功能：
print("Hello", end=' ')
print("World", end=' ')
2.多行字符串对齐功能
print("Hello\tWorld")
print("世界\t你好")
\t的效用等同键盘上的tab键
"""
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{i}*{j}={i*j}\t", end=' ')
        j += 1
    i += 1
    print()

"""
设置一个1-100的随机整数变量，用while循环来配合input语句，判断输入的数字是否等于随机数
有无限次机会直到猜中为止，每一次猜不中都会提示过大还是过小，猜到之后给出猜的次数
"""
import random
num = random.randint(1, 100)
count = 0
flag = True  # True表示while有无数次的循环条件
while flag:
    guess_num = int(input("请输入你猜到的数字："))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False  # 此时变为False表示while循环结束
    else:
        if guess_num > num:
            print("过大了")
        else:
            print("过小了")
print(f"一共猜了{count}次")