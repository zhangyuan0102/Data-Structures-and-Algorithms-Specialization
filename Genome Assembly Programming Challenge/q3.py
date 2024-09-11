#python3
def de_bruijn(k):
    """Generate the k-universal circular binary string using de Bruijn sequence approach."""
    
    # Initialize the graph as an adjacency list
    def build_de_bruijn_graph(k):
        from collections import defaultdict
        adj_list = defaultdict(list)
        
        # Generate all (k-1) length binary strings
        for i in range(2 ** (k - 1)):
            prefix = bin(i)[2:].zfill(k - 1)
            adj_list[prefix].append(prefix[1:] + '0')
            adj_list[prefix].append(prefix[1:] + '1')
        
        # Debug: Print adjacency list
        print("Adjacency List:")
        for key in adj_list:
            print(f"{key}: {adj_list[key]}")
        return adj_list

    def find_eulerian_cycle(adj_list):
        from collections import defaultdict, deque
        
        stack = deque()
        cycle = []
        current_node = next(iter(adj_list))
        stack.append(current_node)

        while stack:
            if adj_list[current_node]:
                stack.append(current_node)
                next_node = adj_list[current_node].pop()
                current_node = next_node
            else:
                cycle.append(current_node)
                current_node = stack.pop()
            
            # Debug: Print stack and current node
            print(f"Stack: {list(stack)}")
            print(f"Current Node: {current_node}")
        
        # Debug: Print final cycle
        print("Final Cycle (reversed):", cycle[::-1])
        return cycle[::-1]  # Reverse the cycle to get the correct order

    # Step 1: Build the De Bruijn graph
    adj_list = build_de_bruijn_graph(k)

    # Step 2: Find Eulerian cycle in the De Bruijn graph
    eulerian_cycle = find_eulerian_cycle(adj_list)

    # Step 3: Construct the k-universal circular binary string
    k_universal_string = eulerian_cycle[0]
    for node in eulerian_cycle[1:]:
        k_universal_string += node[-1]
    
    # Debug: Print the final k-universal string
    print("k-Universal Circular Binary String:", k_universal_string)
    
    return k_universal_string

# Read input
k = int(input().strip())

# Generate and print the k-universal circular binary string
print(de_bruijn(k))



