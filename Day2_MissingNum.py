def missing_num(arr):
    n = len(arr) + 1
    total = n*(n+1)//2
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
    missing = total - curr_sum
    return missing

l = int(input("Enter array length (without missing number): "))
arr = []
for i in range(l):
    x = int(input("Enter number: "))
    arr.append(x)

res = missing_num(arr)
print("Missing number is: ",res)
