from array import *
arr1 = array('i', [2, 4, 5, 8])
arr2 = array('i', [5, 9, 1, 2])
arr3 = array('i', [])
# 'print array values'
for i in arr1:
    print(i, end="")
    print()
for j in arr2:
    print(j, end="")
    print()
# 'addition of arrays with for loop'
for i in range(min(len(arr1), len(arr2))):
    arr3.append(arr1[i] + arr2[i])
print(arr3)
