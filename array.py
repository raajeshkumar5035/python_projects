from array import *
ar1 = array('i', [5, 4, 3, 2, 7, 5])
# ' ar1.sort()'
print(ar1)
# 'this is different program'
arr2 = array('i', [])
l1 = int(input("enter the length of the array:"))

for i in range(l1):
    x = int(input("enter a value"))
    arr2.append(x)
print(arr2)

y = int(input("enter a value to search:"))
print(arr2.index(y))
