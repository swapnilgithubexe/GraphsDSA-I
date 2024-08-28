class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = []
        self.vis = []
        for _ in range(0, self.n):
            self.graph.append([])
            self.vis.append(False)

    def add_edges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, s):
        self.vis[s] = True
        for v in self.graph[s]:
            if not self.vis[v]:
                self.dfs(v)

    def is_connected(self):
        if self.n == 0:
            return True
        ## as an empty graph is connected
        self.vis = [False] * self.n
        self.dfs(0)
        for i in range(0, self.n):
            if not self.vis[i]:
                return False
        return True

if __name__ == "__main__":
    graph = Graph(4)
    graph.add_edges(0, 1)
    graph.add_edges(0, 3)
    graph.add_edges(1, 2)
    graph.add_edges(2, 3)
    print(graph.is_connected())