# python3

import sys

def compute_prefix_hashes(s, p, m):
    """Compute prefix hashes and powers of p."""
    n = len(s)
    hashes = [0] * (n + 1)
    p_pow = [1] * (n + 1)
    for i in range(n):
        hashes[i + 1] = (hashes[i] * p + ord(s[i])) % m
        p_pow[i + 1] = (p_pow[i] * p) % m
    return hashes, p_pow

def get_substring_hash(hashes, p_pow, m, l, r):
    """Get hash of substring s[l:r+1]."""
    return (hashes[r + 1] - hashes[l] * p_pow[r - l + 1] % m + m) % m

def solve(k, t, p):
    m1, p1 = 1_000_000_007, 31
    m2, p2 = 1_000_000_009, 37

    t_hashes1, t_p_pow1 = compute_prefix_hashes(t, p1, m1)
    t_hashes2, t_p_pow2 = compute_prefix_hashes(t, p2, m2)
    p_hashes1, p_p_pow1 = compute_prefix_hashes(p, p1, m1)
    p_hashes2, p_p_pow2 = compute_prefix_hashes(p, p2, m2)
    
    t_len, p_len = len(t), len(p)
    positions = []

    for i in range(t_len - p_len + 1):
        mismatches = 0
        left, right = 0, p_len - 1
        mismatch_found = False
        
        while left <= right and mismatches <= k:
            mid = (left + right) // 2
            if (get_substring_hash(t_hashes1, t_p_pow1, m1, i + left, i + mid) == get_substring_hash(p_hashes1, p_p_pow1, m1, left, mid) and
                get_substring_hash(t_hashes2, t_p_pow2, m2, i + left, i + mid) == get_substring_hash(p_hashes2, p_p_pow2, m2, left, mid)):
                left = mid + 1
            else:
                mismatches += 1
                if mismatches > k:
                    mismatch_found = True
                    break
                left = mid + 1
        
        if not mismatch_found and mismatches <= k:
            positions.append(i)
    
    return positions

for line in sys.stdin.readlines():
	k, t, p = line.split()
	ans = solve(int(k), t, p)
	print(len(ans), *ans)
