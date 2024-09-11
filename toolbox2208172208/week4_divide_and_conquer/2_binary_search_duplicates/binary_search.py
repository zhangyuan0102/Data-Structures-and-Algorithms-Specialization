def binary_search(keys, query):
    l = 0
    r = len(keys) - 1
    result = -1  # To store the result index of the first occurrence
    while l <= r:
        middle = (l + r) // 2
        if keys[middle] == query:
            result = middle  # Update result and move left to find the first occurrence
            r = middle - 1
        elif keys[middle] < query:
            l = middle + 1
        else:
            r = middle - 1
    return result


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
