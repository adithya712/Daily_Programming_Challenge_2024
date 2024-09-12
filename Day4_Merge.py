def merge_arr(arr1, arr2, m, n):
    res = []
    for i in range(m):
        res.append(arr1[i])
    for i in range(n):
        res.append(arr2[i])
    return res

m = int(input("Enter size of array1: "))
arr1, arr2 = [], []
for i in range(m):
    x = int(input("Enter element: "))
    arr1.append(x)
n = int(input("Enter size of array2: "))
for i in range(n):
    x = int(input("Enter element: "))
    arr2.append(x)

k = len(arr1) + len(arr2)
op = merge_arr(arr1, arr2, m, n)
print(op)
