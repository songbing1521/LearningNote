list1 = [1, 3, 5, 7, 100]
list1.append(200)
print(list1)
list1.insert(1, 400)
print(list1)
#合并两个列表
list1.extend([1000,2000])
# 另一种写发
# list1 += [1000,2000]
print(len(list1))
if 3 in list1:
    list1.remove(3)
#根据值删除元素
if 1234 in list1:
    list1.remove(1234)
print(list1)
#从指定