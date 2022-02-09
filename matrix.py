from numpy import *
arr1 = array([[1, 2, 3], [4, 5, 6], [3, 9, 0]])
print(arr1)
m = matrix(arr1)
print(m)
# 'printing matrix with inbuilt function'
m1 = matrix('101 21 6 ;0 9 4;9 1 23')
print(m1)
print(m1.diagonal())        # 'prints the diagonal values in the matrix'
print(m1.argmax())          # 'prints the index value of first occurrence of maximum value'
m2 = m1.copy()              # ' copy array into a new array'
print(m2)
var = m1.dtype              # ' prints the datatype in the matrix'
print(var)
