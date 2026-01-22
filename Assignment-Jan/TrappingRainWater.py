def rain_water(hei):
    l = 0
    r = len(hei) - 1
    leftmax = 0
    rightmax = 0
    ans = 0

    while l <= r:
        if hei[l] <= hei[r]:
            if hei[l] >= leftmax:
                leftmax = hei[l]
            else:
                ans += leftmax - hei[l]
            l += 1
        else:
            if hei[r] >= rightmax:
                rightmax = hei[r]
            else:
                ans += rightmax - hei[r]
            r -= 1

    return ans


n = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n1 = [1, 10 ,0]
print(rain_water(n))