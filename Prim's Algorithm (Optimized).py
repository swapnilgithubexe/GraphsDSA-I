import heapq

def minimum_spanning_tree(edges, n):
    # Create adjacency list for the graph
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))  # Add both v and w for undirected graph
        adj[v].append((u, w))

    visited = [False for _ in range(n)]  # Track visited nodes
    heap = []
    mst_edges = []

    # Push the first node (we start from node 0, as per 0-indexing)
    heapq.heappush(heap, (0, 0, -1))  # (weight, node, parent) if 1 based indexing then push (0, 1, -1)

    while heap:
        w, u, parent = heapq.heappop(heap)  # Extract node with smallest weight

        if visited[u]:
            continue  # If node is already visited, skip it

        visited[u] = True  # Mark the node as visited

        if parent != -1:
            mst_edges.append((u, parent, w))  # Store the edge in MST

        # Explore adjacent nodes
        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(heap, (w, v, u))  # Add adjacent node to heap

    # Print the edges in the MST, ensuring smaller vertex comes first
    for u, v, w in mst_edges:
        if u > v:
            u, v = v, u
        print(u, v, w)

if __name__ == "__main__":
    # Test case 1: Small graph
    edges1 = [
        (0, 1, 6),
        (1, 2, 2),
        (0, 2, 3)
    ]
    n1 = 3
    print("MST for Test Case 1:")
    minimum_spanning_tree(edges1, n1)
    print("\n")

    # Test case 2: Larger graph
    edges2 = [
        (0, 1, 10),
        (0, 2, 5),
        (1, 2, 6),
        (1, 3, 15),
        (2, 3, 7)
    ]
    n2 = 4
    print("MST for Test Case 2:")
    minimum_spanning_tree(edges2, n2)
    print("\n")

    # Test case 3: Fully connected small graph
    edges3 = [
        (0, 1, 1),
        (0, 2, 4),
        (1, 2, 2),
        (1, 3, 6),
        (2, 3, 3)
    ]
    n3 = 4
    print("MST for Test Case 3:")
    minimum_spanning_tree(edges3, n3)
    print("\n")
