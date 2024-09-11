# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    def sift_down(i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < len(data) and data[left] < data[min_index]:
            min_index = left
        if right < len(data) and data[right] < data[min_index]:
            min_index = right
        
        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            sift_down(min_index)
    
    # Start from the last internal node and sift down each node to the heap property.
    for i in range(len(data) // 2 - 1, -1, -1):
        sift_down(i)


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
