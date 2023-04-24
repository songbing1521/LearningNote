def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


a, b = map(int, input().split())
swap(a, b)
print(a, b)
