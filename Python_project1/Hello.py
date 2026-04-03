"""
注释：先展示各类字面量的写法，然后通过print输出
"""
# 666
# 3.14
# "Hello,World!"
print(7)
print(3.14)
print("Hello,World!")
money = 100
print("钱包里有", money, "元")
money = money - 10
print("钱包里还有", money, "元")

"""
标识符命名规则：
1.内容限定：英文、中文、数字，下划线（不推荐使用中文、不可以用数字开头）
2.大小写敏感
3.不可以使用关键字（break, continue, else等）
标识符命名规范：
1.见名知意
2.下划线命名法（多个单词组合成变量名，要使用下划线做分隔）
3.英文字母全部小写
"""
First = 7
first = 7.0
print(First, first)
a_person = "小马"
a_person1 = "小鹿"
print(a_person, a_person1)

# 算术运算符
print("1 + 1 = ", 1 + 1)
print("1 - 0 = ", 1 - 0)
print("2 * 1 = ", 2 * 1)
print("4 / 2 = ", 4 / 2)
print("11 // 2 = ", 11 // 2)
print("9 % 2 = ", 9 % 2)
print("2 ** 3 = ", 2 ** 3)
# 赋值运算符
a = 1 + 1
print(a)
a += 1
print(a)
a -= 1
print(a)
a *= 5
print(a)
a /= 2
print(a)
a %= 3
print(a)
a **= 2
print(a)
a //= 2
print(a)


