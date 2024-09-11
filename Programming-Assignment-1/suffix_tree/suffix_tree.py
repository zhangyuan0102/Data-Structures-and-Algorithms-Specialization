# python3
import sys
def build_suffix_tree(text):
    """

    """

    tree = {'': {'children': {}}}
    result = []

    def add_suffix(node, suffix, start):
        """
  
        """
        if not suffix:
            return
        first_char = suffix[0]
        if first_char not in node['children']:

            node['children'][first_char] = {'start': start, 'length': len(suffix)}
            result.append(text[start:start + len(suffix)])
        else:

            existing_edge = node['children'][first_char]
            existing_start, existing_length = existing_edge['start'], existing_edge['length']
            common_prefix = 0
            while common_prefix < existing_length and suffix[common_prefix] == text[existing_start + common_prefix]:
                common_prefix += 1
            if common_prefix == existing_length:

                add_suffix(existing_edge, suffix[common_prefix:], start + common_prefix)
            else:

                new_node = {'start': existing_start, 'length': common_prefix}
                existing_edge['start'] += common_prefix
                existing_edge['length'] -= common_prefix
                new_char = text[existing_start + common_prefix]
                new_node['children'] = {new_char: existing_edge}
                node['children'][first_char] = new_node
                result.append(text[start:start + len(suffix)])

    for i in range(len(text)):
        add_suffix(tree[''], text[i:], i)

    return result

if __name__ == '__main__':
    text = input().strip()  
    result = build_suffix_tree(text)
    print("\n".join(result))
