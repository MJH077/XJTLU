print("请输入您的姓名：")
name = input()
print("欢迎您，%s" % name)
# name = input("请输入您的姓名：")  这一行与上面的前两行代码效用结果相同
print(type(name))
# 无论输入什么，都会被当做字符串来看待

name = input("球员名字为：")
num = input("球衣号码为：")
print(f"{name}，{num}，你属于洛杉矶湖人队")
