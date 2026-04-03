# continue关键字用于：中断本次循环并直接进入下一循环，可以用于for和while循环中，效果一致
for x in range(1, 6):
    print("语句1")
    continue
    print("语句2")
for x in range(1, 6):
    print("语句1")
    for y in range(1, 6):
        print("语句2")
        continue
        print("语句3")
    print("语句4")

# break关键字用于直接结束循环，可以用于for和while循环，效果一致
for a in range(1, 6):
    print("语句1")
    break
    print("语句2")
print("语句3")

# 在嵌套循环之中，两者只能够作用在所在的循环之上，无法对上层循环起到作用
