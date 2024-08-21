class Graph:
    def __init__(self, n: int) -> None:
        self.graph = []
        for _ in range(n+1):
            self.graph.append([])

    def edges(self, u, v)-> None:
        self.graph[u].append(v)
        self.graph[v].append(u)
        ##For directed graph remove the second line or add the code for single directed edge.

    def printGraph(self):
        print(self.graph)

if __name__ == "__main__":
    graph = Graph(4)
    graph.edges(1,2)
    graph.edges(1,3)
    graph.edges(1,4)
    graph.edges(2,4)
    graph.printGraph()
