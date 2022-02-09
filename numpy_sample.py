from numpy import *
ar1 = array([1, 8, 3, 4, 5])
print(ar1)
# 'sorting the array'
ar1.sort()
print(ar1)
print(ar1.max())    # 'print the maximum value in the array'
print(ar1.min())    # 'print the minimum value in the array'
print(ar1.sum())    # 'print the sum of the array values'


ar2 = array([3, 5, 6, 7.8])
print(ar2)    # 'this will convert everything to same variable type'

# 'adding two arrays with built-in function'
arr1 = array([3, 5, 7, 9])
arr2 = array([12, 32, 54, 51])
arr3 = arr1 + arr2
print(arr3)
