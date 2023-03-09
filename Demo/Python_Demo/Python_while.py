import random

answer = random.randint(0, 100)
counter = 0
while True:
    x = int(input("请输入猜测值"))
    counter += 1
    if x == answer:
        print("猜对了！")
        break
    elif x >= answer:
        print("猜测值过大")
    else:
        print("猜测值过小")
print("答案是%d, 一共猜了%d次" % (answer, counter))
