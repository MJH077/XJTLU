# 二进制变为十进制
a = list(input())
b = list(input())
c = list(input())
d = list(input())
binary_lists = [a, b, c, d]
decimal_values = []
fitness_results = []
for binary_list in binary_lists:
    decimal_value = 0
    length = len(binary_list)
    items = binary_list[::-1]
    for index, item in enumerate(items):
        decimal_value += int(item) * (2 ** index)
    decimal_values.append(decimal_value)
for i in decimal_values:
    result = i - 3
    fitness_results.append(result)
print("Final result: ", fitness_results)


# crossover的变换
a1 = list(input())
b1 = list(input())
x = int(input("输入第一个交叉点："))
y = int(input("输入第二个交叉点："))
child1 = []
child2 = []
if y == 0:
    items1 = a1[:x:]
    items2 = b1[x::]
    items3 = b1[:x:]
    items4 = a1[x::]
    for item1 in items1, items2:
        child1.append(item1)
    for item2 in items3, items4:
        child2.append(item2)
else:
    items1 = a1[:x:]
    items2 = b1[x:y:]
    items3 = b1[:x:]
    items4 = a1[x:y:]
    items5 = a1[y::]
    items6 = b1[y::]
    for item1 in items1, items2, items5:
        child1.append(item1)
    for item2 in items3, items4, items6:
        child2.append(item2)
print(child1, child2)



