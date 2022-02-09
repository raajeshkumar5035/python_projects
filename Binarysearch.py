pos = 0


def search(list1, k):
    i = 0
    u = len(list1)-1

    while i <= u:
        mid = (i+u)//2

        if list1[mid] == k:
            globals()['pos'] = mid
            return True
        else:
            if list1[mid] < k:
                i = mid+1
            else:
                u = mid-1
    return False


list2 = [3, 6, 12, 32, 65, 2, 98, 14, 23, 613, 871, 1456]
list2.sort()
print(list2)
# 'print(len(list2))'
m = len(list2)-1
# 'print(m)'
n = int(input("enter a number to search:"))
if search(list2, n):
    print("found at position:", pos)
else:
    print("not found")
