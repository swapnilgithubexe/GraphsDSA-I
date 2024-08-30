import sys
sys.setrecursionlimit(100000)

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = []
        self.vis = []
        for _ in range(n):
            self.graph.append([])
            self.vis.append(False)
            
    def add_edges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def dfs(self, s, smallOutput):
        self.vis[s] = True
        smallOutput.append(s)

        for v in self.graph[s]:
            if not self.vis[v]:
                self.dfs(v, smallOutput)

    def find_connected_graphs(self):
        output = []
        for v in range(self.n):
            if not self.vis[v]:
                smallOutput = []
                self.dfs(v, smallOutput)
                output.append(smallOutput)

        return output

if __name__ == "__main__":
    graph = Graph(6)
    graph.add_edges(0, 1)
    graph.add_edges(0, 2)
    graph.add_edges(1, 2)
    graph.add_edges(3, 4)
    ans = graph.find_connected_graphs()
    for component in ans:
        component.sort()  # Sort the component as required
        print(' '.join(map(str, component)))