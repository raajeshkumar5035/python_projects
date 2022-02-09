def fact_number(k):
    b = 1
    for i in range(2, k+1):
        b = b * i
    print(b)


n = int(input("enter a number to find a factorial:"))
fact_number(n)
