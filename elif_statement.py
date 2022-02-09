import math
import sys
x = int(input("enter x value:"))
y = int(input("enter y value:"))
z = int(input("enter z value:"))

if x>y and x>z:
    print("x is greater than y and z")
elif y>x and y>z:
    print("y is greater than x and z")
elif z>x and z>y:
    print("z is greater than x and y")
else:
    print("please enter 3 different values")
