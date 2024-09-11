#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
    if not tree:
        return True

    # stack contains tuples of (node_index, min_key, max_key)
    stack = [(0, float('-inf'), float('inf'))]

    while stack:
        node_index, min_key, max_key = stack.pop()
        if node_index == -1:
            continue

        key, left, right = tree[node_index]

        if key <= min_key or key >= max_key:
            return False

        # Push right and left children to the stack with updated constraints
        stack.append((right, key, max_key))
        stack.append((left, min_key, key))

    return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
