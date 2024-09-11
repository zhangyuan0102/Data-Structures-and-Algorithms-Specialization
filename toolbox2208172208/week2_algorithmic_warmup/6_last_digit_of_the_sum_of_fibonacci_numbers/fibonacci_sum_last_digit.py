def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        _sum += current

    return _sum 


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
