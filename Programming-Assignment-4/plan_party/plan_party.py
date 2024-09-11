#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []

def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for _ in range(size - 1):
        a, b = map(int, input().split())
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree

def dfs(tree, vertex, parent, dp):
    dp[vertex][0] = 0  # 不包含当前节点的情况
    dp[vertex][1] = tree[vertex].weight  # 包含当前节点的情况

    for child in tree[vertex].children:
        if child != parent:
            dfs(tree, child, vertex, dp)
            dp[vertex][0] += max(dp[child][0], dp[child][1])
            dp[vertex][1] += dp[child][0]

def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    dp = [[0, 0] for _ in range(size)]
    dfs(tree, 0, -1, dp)
    return max(dp[0][0], dp[0][1])

def main():
    tree = ReadTree()
    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)

# This is to avoid stack overflow issues
threading.Thread(target=main).start()
