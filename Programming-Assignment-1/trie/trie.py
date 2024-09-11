#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = {0: {}}  # Initialize the trie with the root node
    node_id = 1  # Start from node 1, since 0 is the root
    
    for pattern in patterns:
        current_node = 0
        for symbol in pattern:
            if symbol in tree[current_node]:
                current_node = tree[current_node][symbol]
            else:
                tree[current_node][symbol] = node_id
                tree[node_id] = {}  # Initialize the new node
                current_node = node_id
                node_id += 1
    
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
