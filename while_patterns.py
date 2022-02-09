i=1
while i<=5 :
    j=1
    while(j<=5):
                print("*", end="")
                j=j+1
    i=i+1
    print()

#output:-
#*****
#*****
#*****
#*****
#*****
i=int(input("enter a number for a format:"))#entered number is 5
for j in range(i):
    for k in range(i-j):
        print("*", end="")
    print()
#output:-
#*****
#****
#***
#**
#*
i=int(input("enter a number for a format:"))#entered number is 5
for j in range(i):
    for k in range(j+1):
        print ("*", end="")
    print()
#output:-
#*
#**
#***
#****
#*****
