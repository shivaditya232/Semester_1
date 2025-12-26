arr=[2,1,5,3,4]
N=len(arr)
for i in range(1, N):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)

