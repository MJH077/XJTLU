# 归属于if判断的代码语句块，需要在前方填充四个空格缩进，因为python是通过缩进来判断代码块的归属关系
print("请输入您的年龄")
age = input()
new_age = int(age)
if new_age >= 18:
    print("成年")

# if else
print("请输入您的名字")
name = int(input())
if name == 7:
    print("你好，小马")
else:
    print("无法识别")

# if elif else
if int(input("请输入您的身高")) < 120:
    print("身高小于120，免费游玩")
elif int(input("请输入您的vip等级")) > 3:
    print("vip等级大于3，免费游玩")
elif int(input("请输入日期")) == 1:
    print("今天是1号免费日，免费游玩")
else:
    print("请缴费10元")

# 嵌套语句:关键点在于空格缩进，通过空格缩进来决定语句之间的层次关系
if int(input("您的身高为：")) > 120:
    print("身高不符，需交费")
    print("如果您的vip级别大于3，则可免费")
    if int(input("您的vip级别为：")) > 3:
        print("vip级别达标，免费")
    else:
        print("级别不符，需交费")
else:
    print("欢迎您，免费")