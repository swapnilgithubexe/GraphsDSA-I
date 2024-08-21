import queue
class Graph:
    def __init__(self, n):
        self.graph = []
        self.q = queue.Queue()
        self.vis = []
        for _ in range(n+1):
            self.graph.append([])
            self.vis.append(False)

    def edges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, i):
        self.vis[i] = True
        self.q.put(i)

        while not self.q.empty():
            front_node = self.q.get()
            print(front_node)
            for v in self.graph[front_node]:
                if not self.vis[v]:
                    self.q.put(v)
                    self.vis[v] = True

if __name__ == "__main__":
    graph = Graph(5)
    graph.edges(1, 2)
    graph.edges(1, 5)
    graph.edges(2, 3)
    graph.edges(5, 4)
    graph.edges(3, 4)
    graph.bfs(1)
