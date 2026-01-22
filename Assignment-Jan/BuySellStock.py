def BuySellStock(arr):

    min_so_far = float('inf')
    profit = 0
    max_profit = 0

    for i in arr:
        if i < min_so_far:
            min_so_far = i
        else:
            profit = i - min_so_far
            max_profit = max(max_profit,profit)

    return max_profit

#multiple transaction
def BuySellStock1(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


n = [7,1,5,3,6,4]
n2 = [100,120,130,140,150,100]
n1 = [0,1,0,1,0,1]
print(BuySellStock1(n))