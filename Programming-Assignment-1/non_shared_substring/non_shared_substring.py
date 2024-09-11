# python3
import sys
from collections import deque

class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.index = -1  # To store the start index of the suffix
        self.text1_only = False  # True if the node contains substrings from Text1 only
        self.text2_only = False  # True if the node contains substrings from Text2 only

class SuffixTree:
    def __init__(self, s):
        self.root = SuffixTreeNode()
        self.s = s
        self.build_suffix_tree()

    def build_suffix_tree(self):
        n = len(self.s)
        for i in range(n):
            current = self.root
            for j in range(i, n):
                if self.s[j] not in current.children:
                    current.children[self.s[j]] = SuffixTreeNode()
                current = current.children[self.s[j]]
                current.index = i

    def mark_nodes(self, len_text1):
        queue = deque([(self.root, "")])
        while queue:
            node, path = queue.popleft()
            for char, child in node.children.items():
                new_path = path + char
                if '#' in new_path and '$' in new_path:
                    continue
                elif '#' in new_path:
                    child.text2_only = True
                elif '$' in new_path:
                    child.text1_only = True
                queue.append((child, new_path))
        
        def post_order(node):
            for child in node.children.values():
                post_order(child)
                if child.text1_only:
                    node.text1_only = True
                if child.text2_only:
                    node.text2_only = True
        post_order(self.root)

    def find_shortest_non_shared_substring(self, len_text1):
        queue = deque([(self.root, "")])
        shortest = None
        while queue:
            node, path = queue.popleft()
            if node.text1_only and not node.text2_only:
                if shortest is None or len(path) < len(shortest):
                    shortest = path
            for char, child in node.children.items():
                queue.append((child, path + char))
        return shortest

def find_shortest_non_shared_substring(text1, text2):
    combined_text = text1 + '#' + text2 + '$'
    len_text1 = len(text1)
    
    stree = SuffixTree(combined_text)
    stree.mark_nodes(len_text1)
    return stree.find_shortest_non_shared_substring(len_text1)

if __name__ == '__main__':
    input = sys.stdin.read().strip().split()
    text1 = input[0]
    text2 = input[1]
    
    ans = find_shortest_non_shared_substring(text1, text2)
    sys.stdout.write(ans + '\n')
