import heapq


def networkdelaytime(edges, n, k):
    adj = [[] for _ in range(n+1)]
    for u, v, w in edges:
        adj[u].append((w, v))

    distance = [float("inf") for _ in range(n+1)]
    distance[k] = 0

    heap = []
    heapq.heappush(heap, (0, k))

    while heap:
        dist, node = heapq.heappop(heap)
        for w, v in adj[node]:
            if w + dist < distance[v]:
                distance[v] = w + dist
                heapq.heappush(heap, (distance[v], v))

    max_dist = max(distance[1:])

    return max_dist if max_dist != float("inf") else -1

if __name__ == "__main__":
    # Test Case 1: Simple connected graph
    edges = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    print(networkdelaytime(edges, n, k))  # Expected output: 2 (2 -> 1 -> 3 -> 4)

    # Test Case 2: Disconnected graph
    edges = [[1, 2, 1], [2, 3, 1]]
    n = 4
    k = 1
    print(networkdelaytime(edges, n, k))  # Expected output: -1 (node 4 is unreachable)

    # Test Case 3: Single-node graph
    edges = []
    n = 1
    k = 1
    print(networkdelaytime(edges, n, k))  # Expected output: 0 (start node is the only node)

    # Test Case 4: Large weights
    edges = [[1, 2, 100], [2, 3, 200], [1, 3, 500]]
    n = 3
    k = 1
    print(networkdelaytime(edges, n, k))  # Expected output: 300 (1 -> 2 -> 3 is the shortest path)

    # Test Case 5: Graph with cycle
    edges = [[1, 2, 1], [2, 3, 1], [3, 1, 1]]
    n = 3
    k = 1
    print(networkdelaytime(edges, n, k))  # Expected output: 2 (1 -> 2 -> 3)

    # Test Case 6: All nodes directly connected to the source
    edges = [[1, 2, 1], [1, 3, 1], [1, 4, 1]]
    n = 4
    k = 1
    print(networkdelaytime(edges, n, k))  # Expected output: 1 (all nodes are directly reachable from node 1)

    # Test Case 7: All nodes unreachable from the source
    edges = [[2, 3, 1], [3, 4, 1]]
    n = 4
    k = 1
    print(networkdelaytime(edges, n, k))  # Expected output: -1 (nodes 2, 3, and 4 are unreachable from node 1)

