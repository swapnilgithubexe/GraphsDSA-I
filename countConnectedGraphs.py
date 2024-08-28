class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = []
        self.vis = []
        for _ in range(n+1):
            self.vis.append(False)
            self.graph.append([])

    def edges(self,u,v):
        self.graph[v].append(u)
        self.graph[u].append(v)

    def dfs(self, s):
        self.vis[s] = True
        print(f"Visited: {s}")

        for v in self.graph[s]:
            if not self.vis[v]:
                self.dfs(v)

    def connected_graphs_count(self, s):
        connection_count = 0
        for i in range(1, self.n +1):
            if not self.vis[i]:
                self.dfs(i)
                connection_count += 1

        print(f"The number of connected graphs is/are: {connection_count}")

if __name__ == "__main__":
    graph = Graph(6)
    graph.edges(1, 2)
    graph.edges(2, 3)
    graph.edges(3, 4)
    graph.edges(4, 1)
    graph.edges(5, 6)
    graph.connected_graphs_count(1)

