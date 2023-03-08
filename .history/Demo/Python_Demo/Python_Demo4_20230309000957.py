"""
 这是占位符和fstring的一点应用   
"""
###
# a = float(input("请输入华氏度"))
# b = (a-32)/1.8
# print("华氏度：%.1f 转化为 摄氏度为 %.1f"%(a, b))
# print(f"华氏度:{a:.1f} 转化为摄氏度为{b:.1f}")

# 圆面积计算公式
# a = float(input("请输入圆半径："))
# b = a*3.14*3.14
# print(f"圆面积为{b:.1f}")

#输入年份  如果是闰年输出TRUE  否则输出FALSE
year = int(input("请输入年份："))
is_leep = (year%4==0 and year%100 == 0 ) or (year % 400 ==0)
print(f"年份是否为闰年：{is_leep}")