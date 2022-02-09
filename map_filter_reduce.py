from functools import reduce
num = []
n = int(input(print("enter the range of list:")))
for i in range(n):
    k = int(input(print("enter a value:")))
    num.append(k)

print(num)

even = list(map(lambda l: l + 3, num))
print(even)

triple = list(filter(lambda j: j % 2 == 0, num))
print(triple)

list1 = reduce(lambda j, s: j + s, num)
print(list1)
