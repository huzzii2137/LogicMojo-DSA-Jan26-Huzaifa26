def FirstMissingRepeating(arr):

    n = len(arr)
    repeating = -1
    missing = -1

    for i in range(n):
        x= abs(arr[i])
        idx = x-1

        if arr[idx] < 0:
            repeating = x
        else:
            arr[idx] = -arr[idx]

    for i in range(n):
        if arr[i] > 0:
            missing = i+1


    return repeating,missing

n=[1,3,4,3]
print(FirstMissingRepeating(n))
