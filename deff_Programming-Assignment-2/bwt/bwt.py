# python3
import sys

def BWT(text):
    table = sorted(text[i:] + text[:i] for i in range(len(text)))
    last_column = [row[-1] for row in table]
    return ''.join(last_column)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))