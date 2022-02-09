pos = -1


def search(mylist, k):
    i = 0

    while i < len(mylist):
        if mylist[i] == k:
            globals()['pos'] = i
            return True
        i = i + 1

    return False


list1 = [4, 5, 8, 9, 1, 2]
print(len(list1))
n = int(input("enter a number to search:"))

if search(list1, n):
    print("found at:", +pos)
else:
    print("not found")
