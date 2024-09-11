# python3
import sys

def InverseBWT(bwt):
    n = len(bwt)
    first_col = sorted(bwt)
    count = {char: 0 for char in bwt}

    # Initialize T table
    T = []
    for char in bwt:
        count[char] += 1
        T.append((char, count[char]))

    count = {char: 0 for char in bwt}
    F_index = {}
    for i, char in enumerate(first_col):
        count[char] += 1
        F_index[(char, count[char])] = i

    # Reconstruct the original string
    result = []
    idx = bwt.index('$')
    for _ in range(n):
        char, num = T[idx]
        result.append(char)
        idx = F_index[(char, num)]

    return ''.join(result[::-1])


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))