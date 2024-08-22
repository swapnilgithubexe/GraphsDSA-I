class Graph:
    def __init__(self, n: int):
        self.graph = []
        self.vis = []
        self.parent = []
        for _ in range(n+1):
            self.graph.append([])
            self.vis.append(False)
            self.parent.append(-1)

    def edges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    ##startingPoint
    def dfs(self, s):
        self.vis[s] = True
        print(f"Visited: {s}")
        for v in self.graph[s]:
            if not self.vis[v]:
                self.dfs(v)
                self.vis[v] = True
                self.parent[v] = s

    def _dfs(self, s):
        self.vis[s] = True
        self.parent[s] = 0
        self.dfs(s)

    def print_path(self, s, d):
        curr = d
        path = []
        while curr != s:
            path.append(curr)
            curr = self.parent[curr]

        path.append(s)
        path.reverse()
        print(path)

    def find_path(self, src, dest):
        self._dfs(src)
        if not self.vis[dest]:
            print(f"No paths are available.")
        else:
            print("Path is: ", end=" ")
            self.print_path(src, dest)





if __name__ == "__main__":
    graph = Graph(5)
    graph.edges(1, 2)
    graph.edges(1, 3)
    graph.edges(2, 4)
    graph.edges(3, 4)
    graph.edges(4, 5)
    graph.edges(3, 5)

    graph.find_path(1, 5)
