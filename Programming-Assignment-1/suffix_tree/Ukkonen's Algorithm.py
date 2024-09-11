class SuffixTreeNode:
    def __init__(self):
        self.children = [None] * 256  # Assuming ASCII characters
        self.suffix_link = None
        self.start = 0
        self.end = [0]
        self.suffix_index = -1

class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.root = None
        self.last_new_node = None
        self.active_node = None
        self.active_edge = -1
        self.active_length = 0
        self.remaining_suffix_count = 0
        self.leaf_end = -1
        self.root_end = None
        self.split_end = None
        self.size = len(text)
        self.count = 0

    def new_node(self, start, end):
        self.count += 1
        node = SuffixTreeNode()
        node.suffix_link = self.root
        node.start = start
        node.end = end
        node.suffix_index = -1
        return node

    def edge_length(self, n):
        return n.end[0] - n.start + 1

    def walk_down(self, curr_node):
        if self.active_length >= self.edge_length(curr_node):
            self.active_edge = ord(self.text[self.size - self.remaining_suffix_count + 1]) - ord(' ')
            self.active_length -= self.edge_length(curr_node)
            self.active_node = curr_node
            return True
        return False

    def extend_suffix_tree(self, pos):
        self.leaf_end = pos
        self.remaining_suffix_count += 1
        self.last_new_node = None

        while self.remaining_suffix_count > 0:
            if self.active_length == 0:
                self.active_edge = ord(self.text[pos]) - ord(' ')

            if not self.active_node.children[self.active_edge]:
                self.active_node.children[self.active_edge] = self.new_node(pos, [self.leaf_end])

                if self.last_new_node:
                    self.last_new_node.suffix_link = self.active_node
                    self.last_new_node = None
            else:
                next_node = self.active_node.children[self.active_edge]
                if self.walk_down(next_node):
                    continue

                if self.text[next_node.start + self.active_length] == self.text[pos]:
                    if self.last_new_node and self.active_node != self.root:
                        self.last_new_node.suffix_link = self.active_node
                        self.last_new_node = None
                    self.active_length += 1
                    break

                split_end = [next_node.start + self.active_length - 1]
                split_node = self.new_node(next_node.start, split_end)
                self.active_node.children[self.active_edge] = split_node
                split_node.children[ord(self.text[pos]) - ord(' ')] = self.new_node(pos, [self.leaf_end])
                next_node.start += self.active_length
                split_node.children[ord(self.text[next_node.start]) - ord(' ')] = next_node

                if self.last_new_node:
                    self.last_new_node.suffix_link = split_node

                self.last_new_node = split_node

            self.remaining_suffix_count -= 1
            if self.active_node == self.root and self.active_length > 0:
                self.active_length -= 1
                self.active_edge = ord(self.text[pos - self.remaining_suffix_count + 1]) - ord(' ')
            elif self.active_node != self.root:
                self.active_node = self.active_node.suffix_link

    def build_suffix_tree(self):
        self.root_end = [-1]
        self.root = self.new_node(-1, self.root_end)
        self.active_node = self.root

        for i in range(self.size):
            self.extend_suffix_tree(i)

    def get_edges(self):
        edges = []
        self._collect_edges(self.root, edges)
        return edges

    def _collect_edges(self, node, edges):
        if node.start != -1:
            edge = self.text[node.start:min(node.end[0], self.size - 1) + 1]
            edges.append(edge)

        for child in node.children:
            if child:
                self._collect_edges(child, edges)

def build_suffix_tree(text):
    tree = SuffixTree(text)
    tree.build_suffix_tree()
    return tree.get_edges()

if __name__ == '__main__':
    import sys
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))