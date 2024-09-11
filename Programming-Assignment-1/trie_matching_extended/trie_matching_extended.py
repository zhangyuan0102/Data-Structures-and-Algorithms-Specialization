# python3
import sys

NA = -1

class Node:
    def __init__(self):
        self.next = {}
        self.pattern_end = False

def build_trie(patterns):
    tree = {0: Node()}  # Initialize the trie with the root node
    node_id = 1  # Start from node 1, since 0 is the root
    
    for pattern in patterns:
        current_node = 0
        for symbol in pattern:
            if symbol in tree[current_node].next:
                current_node = tree[current_node].next[symbol]
            else:
                tree[current_node].next[symbol] = node_id
                tree[node_id] = Node()  # Initialize the new node
                current_node = node_id
                node_id += 1
        tree[current_node].pattern_end = True  # Mark the end of a pattern
    
    return tree

def prefix_trie_matching(text, trie, start_index):
    current_node = 0
    for i in range(start_index, len(text)):
        symbol = text[i]
        if symbol in trie[current_node].next:
            current_node = trie[current_node].next[symbol]
            if trie[current_node].pattern_end:
                return True
        else:
            return False
    return trie[current_node].pattern_end

def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns)
    text_length = len(text)
    
    for i in range(text_length):
        if prefix_trie_matching(text, trie, i):
            result.append(i)
    
    return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
