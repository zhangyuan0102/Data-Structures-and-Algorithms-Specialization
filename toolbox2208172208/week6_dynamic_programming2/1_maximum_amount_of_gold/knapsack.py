from sys import stdin
def maximum_gold(capacity, weights):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill dp table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            dp[i][w] = dp[i-1][w]  # Case 1: not taking the ith item
            if w >= weights[i-1]:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + weights[i-1])  # Case 2: taking the ith item
    
    return dp[n][capacity]
def maximum_gold(capacity, weights):
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    # Fill dp table
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + weights[i])
    
    return dp[capacity]

if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
