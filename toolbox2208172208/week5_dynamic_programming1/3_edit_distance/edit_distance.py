def edit_distance(first_string, second_string):
    m = len(first_string)
    n = len(second_string)
    

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    

    for i in range(m + 1):
        dp[i][0] = i 
    for j in range(n + 1):
        dp[0][j] = j  
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if first_string[i - 1] == second_string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    
                               dp[i][j - 1] + 1,    
                               dp[i - 1][j - 1] + 1) 
    
    return dp[m][n]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
