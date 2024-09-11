def bridges(edges, n):
    adjList = [[] for _ in range(n)]

    for u, v in edges:
        adjList[u].append(v)
        adjList[v].append(u)  # Adding both directions for undirected graph

    vis = [False for _ in range(n)]
    parent = -1
    timer = 0
    low = [-1 for _ in range(n)]
    disc = [-1 for _ in range(n)]

    result = []

    def dfs(node, parent, adjList, vis, low, disc, result, timer):
        vis[node] = True
        low[node] = disc[node] = timer[0]
        timer[0] += 1

        for v in adjList[node]:
            if v == parent:
                continue
            if not vis[v]:
                dfs(v, node, adjList, vis, low, disc, result, timer)
                low[node] = min(low[node], low[v])

                ##Bridge Check
                if low[v] > disc[node]:
                    result.append([node, v])
            else:
                low[node] = min(low[node], disc[v])

    timer = [0]
    for i in range(n):
        if not vis[i]:
            dfs(i, parent, adjList, vis, low, disc, result, timer)

    # Sorting bridges in result
    result = [sorted(edge) for edge in result]
    result = sorted(result)

    # Printing the result
    for val in result:
        print(val[0], val[1])


if __name__ == "__main__":
    # Test Case 1
    edges1 = [(0, 1), (1, 2), (1, 3), (3, 4)]
    n1 = 5
    print("Test Case 1:")
    bridges(edges1, n1)
    print("\n")

    # Test Case 2
    edges2 = [(0, 1), (0, 2), (1, 2)]
    n2 = 3
    print("Test Case 2:")
    bridges(edges2, n2)
    print("\n")

    # Test Case 3
    edges3 = [(0, 1), (1, 2), (3, 4)]
    n3 = 5
    print("Test Case 3:")
    bridges(edges3, n3)
    print("\n")

    # Test Case 4
    edges4 = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (2, 6)]
    n4 = 7
    print("Test Case 4:")
    bridges(edges4, n4)
    print("\n")

    # Test Case 5
    edges5 = []
    n5 = 5
    print("Test Case 5:")
    bridges(edges5, n5)
    print("\n")
