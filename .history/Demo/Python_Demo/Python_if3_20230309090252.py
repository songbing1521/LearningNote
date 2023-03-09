"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""
# x = float(input("请输入x的值："))

# if x > 1:
#     y = 3*x-5
# elif x >= -1 and x <= 1:

#     y = x + 1
# else:
#     y = 5*x + 3
# print(f"f(x) = {y}")
# x = float(input("请输入x的值"))
# if x > 1:
#     y = 3*x-5
# else:
#     if x >= -1:
#         y = x + 2
#     else:
#         y = 5*x +3
# print(f"f(x) = {y}")

# 输入三角形的边长，如果能构成三角形便进行周长和面积计算。
a = float(input("请输入边长 a ："))
b = float(input("请输入边长b："))
c = float(input("请输入边长 c："))
if a + b > c and a + c > b and c + b > a:
    circun = a + b + c
    p = circun / 2
    area = (p * (p - a) * (p - b) * (p - c))**0.5
    print(f"所构成三角形的周长为{circun:.3f}，面积为{area:.3f}。")

else:
    print("无法构成三角形")
