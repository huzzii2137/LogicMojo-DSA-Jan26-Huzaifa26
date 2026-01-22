def movezeros(n):
    i = 0
    j = 0

    while(j<len(n)):
        if (n[j]!=0):
            n[i], n[j] = n[j], n[i]
            i +=1
            j +=1
        else:
            j+=1
    return n

print(movezeros([1,0,4,20,0,0,12,45,22]))