import queue
class Graph:
    def __init__(self, n):
        self.graph = []
        self.q = queue.Queue()
        self.parent = []
        self.vis = []
        for _ in range(n+1):
            self.graph.append([])
            self.vis.append(False)
            self.parent.append(-1)

    def edges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, i):
        self.vis[i] = True
        self.parent[i] = 0
        self.q.put(i)

        while not self.q.empty():
            front_node = self.q.get()
            for v in self.graph[front_node]:
                if not self.vis[v]:
                    self.q.put(v)
                    self.vis[v] = True
                    self.parent[v] = front_node

    # def _bfs(self, s):
    #     self.vis[s] = True
    #     self.parent[s] = 0
    #     self.bfs(s)

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
        self.bfs(src)
        if not self.vis[dest]:
            print("No paths are available")
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