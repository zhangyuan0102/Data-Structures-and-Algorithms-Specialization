# python3

import sys, threading
from collections import deque
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline().strip())
        self.parent = list(map(int, sys.stdin.readline().strip().split()))

    def compute_height(self):
        root = -1
        for i in range(self.n):
            if self.parent[i] == -1:
                root = i
                break


        queue = deque([(root, 1)]) 
        maxHeight = 0

        while queue:
            node, height = queue.popleft()
            maxHeight = max(maxHeight, height)  


            for i in range(self.n):
                if self.parent[i] == node:
                    queue.append((i, height + 1))

        return maxHeight

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
