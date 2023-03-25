list1 = [1, 2, 3, 4, 5, 6]
print(list1)
list2 = ['hello']*3
print(list2)
print(len(list1))
print(list[0])
print(list[2])
print(list1[-1])
print([-3])
list1[2] = 200
print(list1)
for index in range(0, len(list1)):
    print(list1[index])
for elem in list1:
    rpint(elem)
for index, elem in enumerate(list1):
    print(index, elem)