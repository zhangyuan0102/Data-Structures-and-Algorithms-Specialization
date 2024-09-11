#python3
import sys

class StackWithMax():
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def Push(self, a):
        self.stack.append(a)
        # Push the new max value onto the max_stack
        if not self.max_stack or a >= self.max_stack[-1]:
            self.max_stack.append(a)
        else:
            self.max_stack.append(self.max_stack[-1])

    def Pop(self):
        assert len(self.stack)
        self.stack.pop()
        self.max_stack.pop()

    def Max(self):
        assert len(self.stack)
        return self.max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
