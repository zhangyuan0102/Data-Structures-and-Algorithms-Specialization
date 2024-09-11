# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

def solve(s, t):
    def hash_value(sub, p, m):
        """Compute hash value of a substring."""
        hash_val = 0
        for c in sub:
            hash_val = (hash_val * p + ord(c)) % m
        return hash_val

    def precompute_hashes(string, length, p, m):
        """Precompute hash values for all substrings of a given length."""
        hashes = {}
        n = len(string)
        current_hash = hash_value(string[:length], p, m)
        hashes[current_hash] = [0]
        p_l = pow(p, length, m)
        
        for i in range(1, n - length + 1):
            current_hash = (current_hash * p + ord(string[i + length - 1]) - ord(string[i - 1]) * p_l) % m
            if current_hash not in hashes:
                hashes[current_hash] = []
            hashes[current_hash].append(i)
        
        return hashes

    def has_common_substring(length):
        """Check if there's a common substring of given length."""
        p1, m1 = 31, 1_000_000_007
        p2, m2 = 37, 1_000_000_009
        
        s_hashes1 = precompute_hashes(s, length, p1, m1)
        t_hashes1 = precompute_hashes(t, length, p1, m1)
        
        s_hashes2 = precompute_hashes(s, length, p2, m2)
        t_hashes2 = precompute_hashes(t, length, p2, m2)
        
        for hash1 in t_hashes1:
            if hash1 in s_hashes1:
                for i in t_hashes1[hash1]:
                    sub_t = t[i:i+length]
                    hash2_t = hash_value(sub_t, p2, m2)
                    if hash2_t in s_hashes2:
                        for j in s_hashes1[hash1]:
                            sub_s = s[j:j+length]
                            if sub_t == sub_s:
                                return j, i, length
        return -1, -1, 0
    
    left, right = 0, min(len(s), len(t))
    best_i, best_j, best_len = 0, 0, 0
    
    while left <= right:
        mid = (left + right) // 2
        i, j, l = has_common_substring(mid)
        if l == mid:
            best_i, best_j, best_len = i, j, l
            left = mid + 1
        else:
            right = mid - 1
    
    return Answer(best_i, best_j, best_len)

for line in sys.stdin.readlines():
	s, t = line.split()
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)
