def find_dup(arr):
    slow = 0
    fast = 0
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    slow_new = 0
    while True:
        slow = arr[slow]
        slow_new = arr[slow_new]
        if slow == slow_new:
            return slow
n = int(input("Enter array size:"))
arr = []
for i in range(n):
    x = int(input("Enter element:"))
    arr.append(x)

res = find_dup(arr)
print(res)
