def compute_operations(n):
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # It takes 0 operations to reach 1 from 1

    for i in range(1, n):
        if i + 1 <= n:
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
        if i * 2 <= n:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 <= n:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)

    # To find the sequence of operations, we backtrack from n to 1
    sequence = []
    while n > 0:
        sequence.append(n)
        if n == 1:
            break
        if n % 3 == 0 and dp[n] == dp[n // 3] + 1:
            n //= 3
        elif n % 2 == 0 and dp[n] == dp[n // 2] + 1:
            n //= 2
        else:
            n -= 1
    
    sequence.reverse()
    return sequence
if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
