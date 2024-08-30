class Graph:
    def __init__(self, n):
        self.graph = []
        self.vis = []
        self.recStack = []
        self.isCycle = False
        for _ in range(n):
            self.graph.append([])
            self.vis.append(False)
            self.recStack.append(False)

    def add_edges(self, u, v):
        self.graph[u].append(v)

    def dfs(self, s):
        self.vis[s] = True
        self.recStack[s] = True

        for v in self.graph[s]:
            if not self.vis[v]:
                self.dfs(v)
            elif self.recStack[v]:
                self.isCycle = True

        self.recStack[s] = False

    def cycle(self):
        self.dfs(1)
        return self.isCycle

if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edges(1, 2)
    graph.add_edges(2, 3)
    graph.add_edges(3, 4)
    graph.add_edges(3, 1)
    print(graph.cycle())