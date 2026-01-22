def Max1Consecutive(n):

    current_count, max_count = 0, 0

    for i in n:
        if i == 1:
            current_count +=1
            max_count = max(max_count, current_count)
        else:
            current_count =0
    return max_count


n = [1,2,0,1,1,1,1,0,1,1]
n = [2,3,4]
n = [1,2,1]
n = [0, 1, 1, 1]
n= [1, 1, 0, 1, 1, 1]

print(Max1Consecutive(n))