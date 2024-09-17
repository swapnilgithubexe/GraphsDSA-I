def minimum_spanning_tree_prims(edges, n):
    # Initialize adjacency list for the graph
    adj = [[] for _ in range(n)]

    # Build the adjacency list
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Initialize key values (weights), parent array, and MST set
    key = [float("inf")] * n
    parent = [-1] * n
    mst = [False] * n

    # Start from the first node (0-based indexing)
    key[0] = 0

    # Process all vertices
    for _ in range(n):
        # Find the vertex u with the minimum key value that is not yet in the MST
        mini = float("inf")
        u = -1
        for i in range(n):
            if not mst[i] and key[i] < mini:
                mini = key[i]
                u = i

        # Mark the picked vertex u as part of the MST
        mst[u] = True

        # Update the key values and parent indices of adjacent vertices of u
        for neighbor in adj[u]:
            v, w = neighbor
            if not mst[v] and w < key[v]:
                key[v] = w
                parent[v] = u

    # After processing, print the edges of the MST
    for i in range(1, n):
        print(parent[i], i, key[i])


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: 0-based indexing example
    edges = [
        (0, 1, 2),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 4),
        (2, 3, 5)
    ]
    n = 4  # Number of vertices
    minimum_spanning_tree_prims(edges, n)

    # Test Case 2: Another graph
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    n = 4  # Number of vertices
    minimum_spanning_tree_prims(edges, n)
