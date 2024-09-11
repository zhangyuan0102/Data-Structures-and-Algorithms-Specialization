from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def largest_number_naive(numbers):
    sorted_numbers = sorted(map(str, numbers), key=cmp_to_key(compare))
    return ''.join(sorted_numbers)


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
