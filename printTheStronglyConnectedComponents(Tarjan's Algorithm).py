def dfs(node, adjList, vis, stack, onStack, low, disc, result, timer):
    vis[node] = True
    low[node] = disc[node] = timer[0]
    timer[0] += 1
    stack.append(node)
    onStack[node] = True

    for v in adjList[node]:
        if disc[v] == -1:
            dfs(v, adjList, vis, stack, onStack, low, disc, result, timer)
            low[node] = min(low[node], low[v])
        elif onStack[v]:
            low[node] = min(low[node], disc[v])

    ## If the node is the root of an SCC
    if low[node] == disc[node]:
        current_scc = []
        while True:
            u = stack.pop()
            onStack[u] = False
            current_scc.append(u)
            if u == node:
                break
        result.append(sorted(current_scc))


def stronglyConnectedComponents(edges, n):
    adjList = [[] for _ in range(n)]

    for u, v in edges:
        adjList[u].append(v)

    vis = [False for _ in range(n)]
    stack = []
    onStack = [False for _ in range(n)]
    low = [-1 for _ in range(n)]
    disc = [-1 for _ in range(n)]

    result = []
    timer = [0]

    for i in range(n):
        if disc[i] == -1:
            dfs(i, adjList, vis, stack, onStack, low, disc, result, timer)

    # Sorting SCCs and printing them
    result = sorted(result)
    for scc in result:
        print(" ".join(map(str, scc)))


if __name__ == "__main__":
    # Test Case 1: Simple SCC
    edges1 = [(0, 1), (1, 2), (2, 0), (2, 3)]
    n1 = 4
    print("Test Case 1:")
    stronglyConnectedComponents(edges1, n1)
    print("\n")

    # Test Case 2: Multiple SCCs
    edges2 = [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)]
    n2 = 6
    print("Test Case 2:")
    stronglyConnectedComponents(edges2, n2)
    print("\n")

    # Test Case 3: Disconnected graph
    edges3 = [(0, 1), (2, 3), (4, 5)]
    n3 = 6
    print("Test Case 3:")
    stronglyConnectedComponents(edges3, n3)
    print("\n")

    # Test Case 4: Graph with no edges
    edges4 = []
    n4 = 3
    print("Test Case 4:")
    stronglyConnectedComponents(edges4, n4)
    print("\n")

    # Test Case 5: Single node
    edges5 = []
    n5 = 1
    print("Test Case 5:")
    stronglyConnectedComponents(edges5, n5)
    print("\n")
