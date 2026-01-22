a= [1,-3,4,-2,5,1,-1]
prefixlist = [0] * len(a)

def normalsum(a):
    sum =0
    for i in a:
        sum += i
    return sum

def prefixum(a):
    prefixlist[0] = a[0]
    for i in range(1,len(a)):
        prefixlist[i] = a[i] + prefixlist[i-1]

    return prefixlist

def rangeQuery(left, right):
    print(prefixlist[right],prefixlist[left])
    finalsum = prefixlist[right] - prefixlist[left-1]
    return finalsum

print(normalsum(a))
print(prefixum(a))
print(rangeQuery(2,5))

