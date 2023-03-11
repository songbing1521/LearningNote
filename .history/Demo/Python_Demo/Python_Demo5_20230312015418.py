# 寻找水仙花数
x = input("请输入数字")
if int(x[0])**3 + int(x[1])**3+int(x[2])**3 == int(x):
    print("%d 是水仙花数"% x)
else:
    print("%d 不是水仙花数"%x)
