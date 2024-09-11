# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def _hash_func(s, p, x):
    hash_value = 0
    for c in reversed(s):
        hash_value = (hash_value * x + ord(c)) % p
    return hash_value

def precompute_hashes(text, pattern_length, p, x):
    n = len(text)
    H = [0] * (n - pattern_length + 1)
    S = text[-pattern_length:]
    H[-1] = _hash_func(S, p, x)
    y = 1
    for i in range(pattern_length):
        y = (y * x) % p
    for i in range(n - pattern_length - 1, -1, -1):
        pre_hash = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + pattern_length])) % p
        H[i] = (pre_hash + p) % p
    return H

def get_occurrences(pattern, text):
    p = 1000000007  # a large prime number
    x = 263         # a base for the polynomial hashing
    result = []
    p_hash = _hash_func(pattern, p, x)
    H = precompute_hashes(text, len(pattern), p, x)
    for i in range(len(text) - len(pattern) + 1):
        if p_hash == H[i]: 
            if text[i:i + len(pattern)] == pattern:
                result.append(i)
    return result
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

