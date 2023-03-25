list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
list3 = sorted(list1,reverse=True)
#通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表排序
list4 = sorted(list1, key = len)
print(list1)
print(list2)
print(list3)
print(list4)
list1.sort(reverse=True)
print(list1)