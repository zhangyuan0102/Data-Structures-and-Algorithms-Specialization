def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    fib_list = [0, 1]

    for i in range(2, n + 1):
        previous, current = current, (previous + current) % m
        fib_list.append(current)
        if fib_list[i - 1] == 0 and fib_list[i] == 1:
            return fib_list[n % (i - 1)]
    return current % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
