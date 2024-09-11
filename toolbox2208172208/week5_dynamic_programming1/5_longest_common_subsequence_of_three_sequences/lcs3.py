def lcs3(first_sequence, second_sequence, third_sequence):
    a = len(first_sequence)
    b = len(second_sequence)
    c = len(third_sequence)
    

    dp = [[[0] * (c + 1) for _ in range(b + 1)] for __ in range(a + 1)]
    

    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                if first_sequence[i - 1] == second_sequence[j - 1] == third_sequence[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    
    return dp[a][b][c]  

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
