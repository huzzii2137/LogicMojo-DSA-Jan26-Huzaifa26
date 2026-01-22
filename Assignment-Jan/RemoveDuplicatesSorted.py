def RemoveDuplicatesSorted(arr):
    i = 0
    j = 1

    while(j < len(arr)):
        if (arr[j] != arr[j-1]):
            i += 1
            arr[i] = arr[j]
        j +=1
    return i+1
arr = [1,2,2,3,4,4,5]
print(RemoveDuplicatesSorted(arr))