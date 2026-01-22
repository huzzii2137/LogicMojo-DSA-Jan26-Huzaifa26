def MajorityElement(n):
    count =0
    candidate = None
    new_count =0

    for i in n:
        if count == 0:
            candidate = i
            count +=1
        elif i == candidate:
            count +=1
        else:
            count -=1


    for i in range(0, len(n)):

        if candidate == n[i]:
            new_count +=1

    if new_count > len(n)//2 :
        return candidate

    return -1

n = [1,2,3,2,2,3,1,2,2]
n1 =[3, 1, 3, 3, 2]
n2 = [2, 2, 1, 1, 1, 2, 2]
n3= [1,2,3,4,4]

print(MajorityElement(n))