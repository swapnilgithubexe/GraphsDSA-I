import queue
class Graph:
    def __init__(self, n):
        self.graph = []
        self.n = n
        self.q = queue.Queue()
        self.vis = []
        for _ in range(n+1):
            self.graph.append([])
            self.vis.append(False)

    def edges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, i):
        self.q.put(i)
        self.vis[i] = True

        while not self.q.empty():
            front_ele = self.q.get()
            print(f"Visited: {front_ele}")
            for v in self.graph[front_ele]:
                if not  self.vis[v]:
                    self.vis[v] = True
                    self.q.put(v)
    def bfs_disconnected(self):
        for i in range(1, self.n + 1):
            if self.graph[i] and not self.vis[i]:
                self.bfs(i)

if __name__ == "__main__":
    graph = Graph(17)
    graph.edges(4, 6)
    graph.edges(6, 9)
    graph.edges(9, 4)
    graph.edges(11, 17)
    graph.bfs_disconnected()



