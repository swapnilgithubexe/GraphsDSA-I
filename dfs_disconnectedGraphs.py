class Graph:
    def __init__(self, n):
        self.graph = []
        self.vis = []
        self.n = n
        for _ in range(n+1):
            self.graph.append([])
            self.vis.append(False)

    def edges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, i):
        print(f"Visited: {i}")
        self.vis[i] = True
        for v in self.graph[i]:
            if not self.vis[v]:
                self.dfs(v)
                self.vis[v] = True

    def dfs_disconnected(self):
        for i in range(1, self.n +1):
            if not self.vis[i]:
                self.dfs(i)


if __name__ == "__main__":
    graph = Graph(5)
    graph.edges(1, 2)
    graph.edges(2, 3)
    graph.edges(3, 1)
    graph.edges(4, 5)
    graph.dfs_disconnected()


