# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    n = len(sequence)
    if n * m == 0:
        return []
    if m == 1:
        return sequence

    def clean_deque(i):
        # Remove indexes of elements not from sliding window
        if deq and deq[0] == i - m:
            deq.popleft()

        # Remove from deq indexes of all elements 
        # which are smaller than current element sequence[i]
        while deq and sequence[i] > sequence[deq[-1]]:
            deq.pop()

    deq = deque()
    max_idx = 0
    for i in range(m):
        clean_deque(i)
        deq.append(i)
        # Compute max in the first window
        if sequence[i] > sequence[max_idx]:
            max_idx = i
    output = [sequence[max_idx]]

    # Build output
    for i in range(m, n):
        clean_deque(i)
        deq.append(i)
        output.append(sequence[deq[0]])
    
    return output

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

