from array import *

ar1 = array('i', [5, 4, 3, 2, 7])

ar2 = array('i', [])
v1 = int(input("enter the length of the array:"))
for i in range(v1):
    print("enter the value:")
    ar2.append(i)
print(ar2)
