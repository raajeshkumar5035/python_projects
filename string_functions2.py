def fun(lis11):
    for j in lis11:
        count = 0
        for k in j:
            # 'print(k)'
            # 'global count'
            count = count + 1
        print(j, count)


lis1 = list()
v1 = int(input("enter the length of the list:"))
for i in range(v1):
    y = (input("enter a string:"))
    lis1.append(y)
print(lis1)


fun(lis1)
