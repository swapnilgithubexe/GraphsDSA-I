class Graph:
    def __init__(self, n: int) -> None:
        self.graph = []

    def edges(self, u, v)-> None:
        self.graph.append((u, v))

    def printGraph(self):
        print(self.graph)

if __name__ == "__main__":
    graph = Graph(4)
    graph.edges(1,2)
    graph.edges(1,3)
    graph.edges(1,4)
    graph.edges(2,4)
    graph.printGraph()
