from math import sqrt

num = int(input("请输入一个整数："))
end  = int(sqrt(num))
is_prime = True
for i in range(2,end+1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num !=1:
    print("%d is  prime"% num)
else:
    print("%d is not prime"% num) 