import queue
class Graph():
    def __init__(self,n):
        self.graph = []
        self.q = queue.Queue()
        self.ans = []
        self.indegree = []

        for i in range(n+1):
            self.graph.append([])
            self.indegree.append(0)

    def edges(self, u,v):
        self.graph[u].append(v)

    def calculateIndegree(self):
        for u in range(len(self.graph)):
            for v in self.graph[u]:
                self.indegree[v] += 1


    def bfs(self):
        for i in range(1, len(self.graph)):
            if self.indegree[i] == 0:
                self.q.put(i)

        while not self.q.empty():
            front_node = self.q.get()
            self.ans.append(front_node)

            for neighbor in self.graph[front_node]:
                self.indegree[neighbor] -= 1
                if self.indegree[neighbor] == 0:
                    self.q.put(neighbor)

        return self.ans

# Test cases
if __name__ == "__main__":
    # Create a graph with 5 nodes (1-based index)
    g = Graph(5)

    # Add edges
    g.edges(1, 2)
    g.edges(1, 3)
    g.edges(3, 4)
    g.edges(2, 4)
    g.edges(4, 5)

    # Calculate indegree
    g.calculateIndegree()

    # Perform BFS (Topological Sort in this case)
    result = g.bfs()

    # Output the result
    print("Topological Sort / BFS Order:", result)

    # Additional Test
    # Test with disconnected graph
    g2 = Graph(4)
    g2.edges(1, 2)
    g2.edges(3, 4)

    g2.calculateIndegree()
    result2 = g2.bfs()
    print("Topological Sort / BFS Order (Disconnected Graph):", result2)


