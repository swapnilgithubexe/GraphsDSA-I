class Graph:
    def __init__(self, n):
        self.graph = [[] for _ in range(n)]
        self.vis = [False] * n

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, s):
        self.vis[s] = True
        for v in self.graph[s]:
            if not self.vis[v]:
                self.dfs(v)

    def check_path(self, src, dest):
        self.dfs(src)
        return self.vis[dest]

n = 5  # Number of vertices
edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
g = Graph(n)

#       0 - 1
#       |   |
#       2 - 3 - 4

for u, v in edges:
    g.add_edge(u, v)

src, dest = 0, 4
if g.check_path(src, dest):
    print("True")
else:
    print("False")