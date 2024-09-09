def sort_012(a, n):
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        elif a[mid] == 2:
            a[mid], a[high] = a[high], a[mid]
            high -= 1

    return a

arr = []
size = int(input("Enter size of array: "))
for i in range(size):
    x = int(input("Enter element: "))
    if x == 0 or x == 1 or x == 2:
        arr.append(x)

n = len(arr)
res = sort_012(arr, n)
print(res)
