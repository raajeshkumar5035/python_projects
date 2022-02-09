def counting(lis11):
    even = 0
    odd = 0
    for t in lis11:
        if t % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    print(even)
    print(odd)


lis1 = list()
v1 = int(input("enter the length of the list:"))
for i in range(v1):
    y = int(input("enter a value:"))
    lis1.append(y)
print(lis1)


counting(lis1)
