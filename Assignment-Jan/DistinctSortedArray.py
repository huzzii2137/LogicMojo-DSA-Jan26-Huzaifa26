def DistinctSortedArray(arr):
    i, j = 0, len(arr) - 1
    count = 0

    while i <= j:
        left = abs(arr[i])
        right = abs(arr[j])

        if left > right:
            count += 1
            while i <= j and abs(arr[i]) == left:
                i += 1
        elif left < right:
            count += 1
            while i <= j and abs(arr[j]) == right:
                j -= 1
        else:
            count += 1
            while i <= j and abs(arr[i]) == left:
                i += 1
            while i <= j and abs(arr[j]) == right:
                j -= 1

    return count



arr=[-1, -1, 0, 1, 1, 1]
print(DistinctSortedArray(arr))