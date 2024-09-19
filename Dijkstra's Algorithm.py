import heapq

def dijkstraAlgo(adj, n, s):
    heap = []
    distance = [float("inf") for _ in range(n)]
    distance[s] = 0
    heapq.heappush(heap, (0, s))

    while heap:
        top_element = heapq.heappop(heap)
        dist, node = top_element

        for w, v in adj[node]:
            if dist + w < distance[v]:
                distance[v] = dist + w
                heapq.heappush(heap, (distance[v], v))

    return distance

def shortest_path(edges, V):
    adj = [[] for _ in range(V)]

    for u, v, w in edges:
        adj[u].append((w, v))
        adj[v].append((w, u))

    res = dijkstraAlgo(adj, V, 0)
    for v in range(V):
        print(v, res[v])

if __name__ == "__main__":
    edges1 = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (1, 3, 1),
        (2, 3, 5)
    ]
    V1 = 4
    print("Test Case 1:")
    shortest_path(edges1, V1)
    print()

    # Test case 2
    edges2 = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    V2 = 4
    print("Test Case 2:")
    shortest_path(edges2, V2)
    print()

    # Test case 3: Larger graph
    edges3 = [
        (0, 1, 2),
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (2, 3, 7),
        (2, 4, 5),
        (3, 4, 9)
    ]
    V3 = 5
    print("Test Case 3:")
    shortest_path(edges3, V3)