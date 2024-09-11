from sys import stdin


def partition3(values):
    total_sum = sum(values)
    
    if total_sum % 3 != 0:
        return 0
    
    target = total_sum // 3
    n = len(values)
    
    # Initialize DP table
    dp = [[[False] * (target + 1) for _ in range(target + 1)] for _ in range(n + 1)]
    dp[0][0][0] = True
    
    for i in range(1, n + 1):
        current_value = values[i-1]
        for j in range(target + 1):
            for k in range(target + 1):
                dp[i][j][k] = dp[i-1][j][k]
                if j >= current_value:
                    dp[i][j][k] = dp[i][j][k] or dp[i-1][j-current_value][k]
                if k >= current_value:
                    dp[i][j][k] = dp[i][j][k] or dp[i-1][j][k-current_value]
    
    return 1 if dp[n][target][target] else 0
def partition3(values):
    total_sum = sum(values)
    
    # Check if total sum is divisible by 3
    if total_sum % 3 != 0:
        return 0
    
    target = total_sum // 3
    n = len(values)
    
    # Initialize DP table
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    # Fill DP table
    for i in range(1, n + 1):
        current_value = values[i - 1]
        for j in range(n, 0, -1):
            for k in range(target, current_value - 1, -1):
                if dp[j - 1][k - current_value]:
                    dp[j][k] = 1
    
    # Count the number of subsets that sum to target
    count = 0
    for i in range(1, n + 1):
        if dp[i][target]:
            count += 1
    
    return 1 if count >= 3 else 0

if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
