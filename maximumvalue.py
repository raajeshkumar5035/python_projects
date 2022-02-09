from array import *

ar1 = array('i', [5, 4, 3, 2, 7, 1])
k = 0
for i in ar1:
    if k == 0 or i > k:
        k = i
print("maximum value is ", k)
