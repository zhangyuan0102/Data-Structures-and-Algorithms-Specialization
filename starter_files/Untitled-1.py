# python3
import sys
import math
import hashlib
import numpy as np
import statistics as stat

class hash_function:
    def __init__(self, seed, width):
        self.seed = seed
        self.width = width

    def hash(self, x):
        hash_object = hashlib.md5((str(x) + str(self.seed)).encode())
        hash_value = int(hash_object.hexdigest(), 16)
        return hash_value % self.width

class sign_function:
    def __init__(self):
        self.hf = hash_function(np.random.uniform(10, 50), 1000)

    def hash(self, x):
        return 1 if self.hf.hash(x) > 500 else -1

class count_sketch:
    """
    b - number of buckets; large enough to reduce variance, i.e. estimation error,
        or as large as possible given memory constraints
    t - number of hash functions; log(n) + 1
    """
    def __init__(self, n):
        self.b = int(math.log(n) * 1500)
        self.t = int(math.log(n) + 1)
        self.data = [[0] * self.b for _ in range(self.t)]
        self.ith_data = [0] * self.t
        self.funcs = [(hash_function(i, self.b), sign_function()) for i in range(self.t)]

    def update(self, i, frq = 1):
        for j in range(self.t):
            self.data[j][self.funcs[j][0].hash(i)] += self.funcs[j][1].hash(i) * frq

    def estimate(self, i):
        for j in range(self.t):
            self.ith_data[j] = self.data[j][self.funcs[j][0].hash(i)] * self.funcs[j][1].hash(i)
        return stat.median(self.ith_data)

# 主程序部分
if __name__ == "__main__":
    n, t = int(sys.stdin.readline().strip()), int(sys.stdin.readline().strip())

    algo = count_sketch(n)

    # 读取好事数据并更新
    for _ in range(n):
        id, value = [int(i) for i in sys.stdin.readline().strip().split()]
        algo.update(id, value)  # 好事，正数

    # 读取坏事数据并更新
    for _ in range(n):
        id, value = [int(i) for i in sys.stdin.readline().strip().split()]
        algo.update(id, -value)  # 坏事，负数

    # 读取查询
    num_queries = int(sys.stdin.readline().strip())
    queries = list(map(int, sys.stdin.readline().strip().split()))
    assert(len(queries) == num_queries)

    # 输出结果
    for query in queries:
        print("1 " if algo.estimate(query) >= t else "0 ", end="")
    print()
