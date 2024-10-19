def dfs(s, adj, vis):
    vis[s] = True

    for v in adj[s]:
        if not vis[v]:
            dfs(v, adj, vis)

def numOfIslands(edges, n, m):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    visited = [False for _ in range(n)]
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, adj, visited)
            count += 1

    return count

if __name__ == "__main__":
    # Test Case 1: No edges (isolated islands)
    edges = []
    n = 5  # Number of islands (vertices)
    m = 0  # Number of edges
    print(numOfIslands(edges, n, m))  # Expected output: 5 (Each island is its own component)

    # Test Case 2: Single connected component (fully connected islands)
    edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
    n = 5  # 5 islands, 4 edges, all connected
    m = len(edges)
    print(numOfIslands(edges, n, m))  # Expected output: 1 (All islands are connected)

    # Test Case 3: Multiple connected components
    edges = [(0, 1), (2, 3), (3, 4)]
    n = 5  # 5 islands, 3 edges, two separate components
    m = len(edges)
    print(numOfIslands(edges, n, m))  # Expected output: 2 (There are two components: [0,1] and [2,3,4])

    # Test Case 4: No islands (n = 0)
    edges = []
    n = 0  # No islands
    m = 0
    print(numOfIslands(edges, n, m))  # Expected output: 0 (No islands, no components)

    # Test Case 5: Disconnected islands and one connected component
    edges = [(0, 1), (2, 3)]
    n = 5  # 5 islands, 2 edges, two separate components and 1 isolated island
    m = len(edges)
    print(numOfIslands(edges, n, m))  # Expected output: 3 (Two connected components: [0,1], [2,3] and one isolated island [4])

    # Test Case 6: Only one island (n = 1)
    edges = []
    n = 1  # 1 island, no edges
    m = 0
    print(numOfIslands(edges, n, m))  # Expected output: 1 (A single island forms one component)
