def findElement(arr):
    n = len(arr)

    if (n < 3):
        return -1

    leftMax =[0] * n
    rightMin =[0] * n

    leftMax[0] = arr[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], arr[i])

    rightMin[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        rightMin[i] = min(rightMin[i + 1], arr[i])

    # Find valid element
    for i in range(1, n - 1):
        if leftMax[i - 1] <= arr[i] <= rightMin[i + 1]:
            return arr[i]

    return -1

arr = [4, 3, 2, 1, 5, 9, 8, 7]
print(findElement(arr))