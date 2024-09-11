def change(money):
    dp = [money+1]*(money+1)
    dp[0] =0
    coins = [1, 3, 4]
    for coin in coins:
        for k in range(coin,money+1):
            dp[k] = min(dp[k],dp[k-coin]+1)
    return dp[money] if dp[money] != money+1 else -1

if __name__ == '__main__':
    m = int(input())
    print(change(m))
