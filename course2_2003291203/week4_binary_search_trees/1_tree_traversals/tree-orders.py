# python3

import sys, threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            a, b, c = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        result = []
        stack = []
        current = 0

        while stack or current != -1:
            if current != -1:
                stack.append(current)
                current = self.left[current]
            else:
                current = stack.pop()
                result.append(self.key[current])
                current = self.right[current]

        return result

    def preOrder(self):
        result = []
        stack = [0]

        while stack:
            current = stack.pop()
            if current != -1:
                result.append(self.key[current])
                stack.append(self.right[current])
                stack.append(self.left[current])

        return result

    def postOrder(self):
        result = []
        stack = [(0, False)]

        while stack:
            current, visited = stack.pop()
            if current == -1:
                continue
            if visited:
                result.append(self.key[current])
            else:
                stack.append((current, True))
                stack.append((self.right[current], False))
                stack.append((self.left[current], False))

        return result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
