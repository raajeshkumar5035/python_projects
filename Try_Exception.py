a = int(input("enter a number:"))
b = int(input("enter b number:"))
try:
    print("resource open")
    c = a / b
    print(c)
    j = int(input("enter j value:"))
    print(j)

except Exception as e:
    print("something went wrong")

finally:
    print("resource close")
