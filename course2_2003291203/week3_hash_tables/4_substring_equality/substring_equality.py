# python3

import sys

class Solver:
    def __init__(self, s):
        self.s = s
        self.m1 = 1000000007
        self.m2 = 1000000009
        self.x = 263
        self.H1 = self._hash_func(len(s), self.m1)
        self.H2 = self._hash_func(len(s), self.m2)
        self.powers1 = self._precompute_powers(len(s), self.m1)
        self.powers2 = self._precompute_powers(len(s), self.m2)

    def _hash_func(self, n, m):
        H = [0] * (n + 1)
        for i in range(1, n + 1):
            H[i] = (self.x * H[i - 1] + ord(self.s[i - 1])) % m
        return H

    def _precompute_powers(self, n, m):
        powers = [1] * (n + 1)
        for i in range(1, n + 1):
            powers[i] = (powers[i - 1] * self.x) % m
        return powers

    def precompute(self, a, l, m, H, powers):
        # a is 0-based, adjust H index by adding 1
        hash_value = (H[a + l] - powers[l] * H[a]) % m
        return (hash_value + m) % m

    def ask(self, a, b, l):
        hash1_a = self.precompute(a, l, self.m1, self.H1, self.powers1)
        hash1_b = self.precompute(b, l, self.m1, self.H1, self.powers1)
        hash2_a = self.precompute(a, l, self.m2, self.H2, self.powers2)
        hash2_b = self.precompute(b, l, self.m2, self.H2, self.powers2)
        return hash1_a == hash1_b and hash2_a == hash2_b
	



s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
