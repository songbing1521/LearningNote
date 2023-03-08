"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""
x = float(input("请输入x的值："))

if x > 1:
    y = 3*x-5
elif x >= -1 and x <= 1: 
    
    y = x + 1
else:
    y = 5*x + 3
print(f"f(x) = {y}")
    