def TwoSum(arr, target):
    i = 0
    j = len(arr) - 1

    while i < j:
        s = arr[i]+arr[j]
        if s == target:
            return [i + 1, j + 1]
        elif s > target:
            j -= 1
        else:
            i += 1

    return -1

arr = [2,7,11,15]
print(TwoSum(arr,9))