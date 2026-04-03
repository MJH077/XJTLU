"""
while循环的循环条件是自定义的，即自行控制循环条件；for循环是一种“轮询”机制，是对一批内容进行“逐个处理”，也被称为“遍历循环”
for循环是无法定义循环条件的，只能够从被处理的数据集当中依次取出内容进行处理，所以说该循环无法构建无限循环
for循环语法：
for 临时变量 in 待处理数据集（序列）：
    循环满足条件时执行的代码
"""
# 将name的内容逐个取出并赋予x临时变量，就可以再循环体内对x进行处理
name = "小马"
for x in name:
    print(x)

""""
待处理数据集被称为序列类型，是指其内容可以一个个依次取出的一种类型，包括字符串、列表、元组等
range语句：
1. range(num) 即获取一个从0开始，到num结束的数字序列（不含num本身），例如range(5)得到的数据是[0,1,2,3,4]
2. range(num1, num2) 即获得一个从num1开始，到num2结束的数字序列（不含num2本身），例如range(5,10)得到的数据是[5,6,7,8,9]
3. range(num1, num2, step) 即获得一个从num1开始，到num2结束的数字序列（不含num2本身），数字之间的步长以step为准（step默认为1），例如range(5,10,2)得到的数据是[5,7,9]
"""
for x in range(10):
    print(x)
for x in range(5, 10):
    print(x)
for x in range(0, 10, 2):
    print(x)

# 1到num的序列，统计偶数的出现次数
count = 0
for x in range(1, 100):
    if x % 2 != 0:
        count += 1
print(count)

""""
临时变量在编程规范上作用域只限定在for循环内部
但是如果在for循环外部访问临时变量，实际上是可以访问得到的，但是规则上是不允许这么做的
"""
for i in range(5):
    print(i)
print(i)

for x in range(1, 11):
    print(f"今天是第{x}天")
    for j in range(1, 11):
        print(f"送的第{j}朵玫瑰花")
    print("我喜欢你")
print(f"这是第{x}天，成功")

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i}*{j}={i*j}\t", end='')
    print()
