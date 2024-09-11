def majority_element_naive(elements):
    from collections import Counter
    element_count = Counter(elements)    
    # Iterate through the counter to check if any element appears more than n/2 times
    for count in element_count.values():
        if count > len(elements) // 2:
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
