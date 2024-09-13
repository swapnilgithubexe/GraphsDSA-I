class Graph():
    def __init__(self, n):
        self.graph = []
        self.visited = []
        self.stack = []

        for i in range(n+1):
            self.graph.append([])
            self.visited.append(False)

    def add_edges(self, u, v):
        self.graph[u].append(v)

    def dfs(self, s):
        for v in self.graph[s]:
            if not self.visited[v]:
                self.visited[v] = True
                self.dfs(v)
        self.stack.append(s)

    def topologicalSort(self, n):
        for i in range(1, n+1):
            if not self.visited[i]:
                self.visited[i] = True
                self.dfs(i)

        topological_sorted_array = []
        while len(self.stack) > 0:
            topological_sorted_array.append(self.stack[-1])
            self.stack.pop()

        return topological_sorted_array


if __name__ == "__main__":
    # Test Case 1: Simple DAG
    g = Graph(6)
    g.add_edges(5, 2)
    g.add_edges(5, 0)
    g.add_edges(4, 0)
    g.add_edges(4, 1)
    g.add_edges(2, 3)
    g.add_edges(3, 1)

    result = g.topologicalSort(6)
    print("Topological Sort:", result)  # Expected Output: [5, 4, 2, 3, 1, 0]

    # Test Case 2: Another DAG
    g2 = Graph(4)
    g2.add_edges(1, 2)
    g2.add_edges(1, 3)
    g2.add_edges(3, 4)

    result = g2.topologicalSort(4)
    print("Topological Sort:", result)