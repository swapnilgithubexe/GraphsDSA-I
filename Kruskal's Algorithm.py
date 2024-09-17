def find_parent(parent, node):
    # Function to find the parent of the node (with path compression)
    if node == parent[node]:
        return node
    parent[node] = find_parent(parent, parent[node])  # Path compression
    return parent[node]


def unionSet(u, v, parent, rank):
    # Union two subsets by rank
    u = find_parent(parent, u)
    v = find_parent(parent, v)

    # Attach the tree with lower rank under the higher rank tree
    if rank[u] < rank[v]:
        parent[u] = v
    elif rank[v] < rank[u]:
        parent[v] = u
    else:
        parent[u] = v
        rank[v] += 1  # If ranks are equal, increase rank of the new root


def minimumSpanningTree(edges, V=5):
    # Sort the edges by weight
    edges.sort(key=lambda x: x[2])

    parent = list(range(V))  # Each node is its own parent initially
    rank = [0] * V  # Initialize rank for each node
    mst = []  # List to store the MST edges

    for u, v, wt in edges:
        root_u = find_parent(parent, u)
        root_v = find_parent(parent, v)

        # If u and v belong to different sets, include this edge in MST
        if root_u != root_v:
            mst.append((u, v, wt))
            unionSet(u, v, parent, rank)

    # Print the MST edges with the smaller vertex first
    for u, v, wt in mst:
        if u > v:
            u, v = v, u  # Swap to ensure smaller vertex comes first
        print(u, v, wt)


# Test case 1
print("Test case 1: ")
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
V = 4
minimumSpanningTree(edges, V)
# Expected output:
# 0 3 5
# 2 3 4
# 0 1 10

print("\nTest case 2: ")
# Test case 2 (with 5 vertices)
edges = [(0, 1, 2), (1, 2, 3), (0, 3, 6), (1, 3, 8), (3, 4, 9), (2, 4, 5)]
V = 5
minimumSpanningTree(edges, V)
# Expected output:
# 0 1 2
# 1 2 3
# 2 4 5
# 0 3 6

print("\nTest case 3: ")
# Test case 3 (disconnected graph, minimal input)
edges = [(0, 1, 1)]
V = 2
minimumSpanningTree(edges, V)
# Expected output:
# 0 1 1
