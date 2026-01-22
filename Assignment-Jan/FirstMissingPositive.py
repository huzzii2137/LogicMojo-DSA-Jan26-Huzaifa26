def FirstMissingPositive(arr):

    for i in range(0,len(arr)):
        if arr[i] <= 0 or arr[i] > len(arr):
            arr[i] = len(arr)+1

    for i in range(0, len(arr)):
        x= abs(arr[i])
        if (x<= len(arr)):
            index = x-1
            if arr[index] > 0:
                arr[index] = -arr[index]


    for i in range(0, len(arr)):
        if arr[i] > 0:
            return i+1

    return len(arr)+1

n = [3,4,-1,1]
print(FirstMissingPositive(n))