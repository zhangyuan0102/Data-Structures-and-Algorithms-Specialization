class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.start = -1
        self.end = -1
        self.suffix_link = None

class SuffixTree:
    def __init__(self, text):
        self.text = text + '$'  # 添加结束符
        self.root = SuffixTreeNode()
        self.root.suffix_link = self.root
        self.active_node = self.root
        self.active_edge = -1
        self.active_length = 0
        self.remaining_suffix_count = 0
        self.end = -1
        self.size = len(self.text)
        self.build_suffix_tree()
        self.suffix_array = []

    def edge_length(self, node):
        return min(node.end, self.end) - node.start + 1

    def walk_down(self, node):
        if self.active_length >= self.edge_length(node):
            self.active_edge += self.edge_length(node)
            self.active_length -= self.edge_length(node)
            self.active_node = node
            return True
        return False

    def extend_suffix_tree(self, pos):
        self.end = pos
        self.remaining_suffix_count += 1
        last_new_node = None

        while self.remaining_suffix_count > 0:
            if self.active_length == 0:
                self.active_edge = pos

            if self.text[self.active_edge] not in self.active_node.children:
                self.active_node.children[self.text[self.active_edge]] = SuffixTreeNode()
                child = self.active_node.children[self.text[self.active_edge]]
                child.start = pos
                child.end = self.size - 1

                if last_new_node is not None:
                    last_new_node.suffix_link = self.active_node
                    last_new_node = None
            else:
                next_node = self.active_node.children[self.text[self.active_edge]]
                if self.walk_down(next_node):
                    continue
                if self.text[next_node.start + self.active_length] == self.text[pos]:
                    if last_new_node is not None and self.active_node != self.root:
                        last_new_node.suffix_link = self.active_node
                        last_new_node = None
                    self.active_length += 1
                    break
                split_end = next_node.start + self.active_length - 1
                split = SuffixTreeNode()
                self.active_node.children[self.text[self.active_edge]] = split
                split.start = next_node.start
                split.end = split_end
                split.children[self.text[pos]] = SuffixTreeNode()
                split.children[self.text[pos]].start = pos
                split.children[self.text[pos]].end = self.size - 1
                next_node.start += self.active_length
                split.children[self.text[next_node.start]] = next_node

                if last_new_node is not None:
                    last_new_node.suffix_link = split

                last_new_node = split

            self.remaining_suffix_count -= 1

            if self.active_node == self.root and self.active_length > 0:
                self.active_length -= 1
                self.active_edge = pos - self.remaining_suffix_count + 1
            elif self.active_node != self.root:
                self.active_node = self.active_node.suffix_link

    def build_suffix_tree(self):
        for i in range(self.size):
            self.extend_suffix_tree(i)

    def build_suffix_array(self, node=None, suffix_array=None):
        if node is None:
            node = self.root
            suffix_array = []
        if node.start != -1:
            suffix_array.append(node.start)
        for child in sorted(node.children.values(), key=lambda x: self.text[x.start]):
            self.build_suffix_array(child, suffix_array)
        return suffix_array

    def get_suffix_array(self):
        # Remove the last entry which is the suffix starting with the added '$'
        suffix_array = self.build_suffix_array()
        suffix_array.pop()
        return suffix_array

# 示例用法
text = "banana"
suffix_tree = SuffixTree(text)
suffix_array = suffix_tree.get_suffix_array()
print("Suffix Array:", suffix_array)

