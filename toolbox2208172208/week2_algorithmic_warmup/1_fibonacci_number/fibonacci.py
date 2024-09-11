def fibonacci_number(n):
    a,b =0,1
    for _ in range(n):
        a,b =b, a+b
    return a

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
