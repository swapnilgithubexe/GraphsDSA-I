class Graph:
    def __init__(self, n: int) -> None:
        self.graph = []

    def edges(self, u, v, wt)-> None:
        self.graph.append((u, v, wt))

    def printGraph(self):
        print(self.graph)

if __name__ == "__main__":
    graph = Graph(4)
    graph.edges(1,2, 10)
    graph.edges(1,3, 20)
    graph.edges(1,4, 22)
    graph.edges(2,4, 25)
    graph.printGraph()
