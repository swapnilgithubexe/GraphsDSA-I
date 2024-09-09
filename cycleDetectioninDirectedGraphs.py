
def isCycle(edges, n, m):
    adjList = [[] for _ in range(n)]
    vis = [False for _ in range(n)]
    recStack = [False for _ in range(n)]

    for u, v in edges:
        adjList[u].append(v)

    def dfs(node):
        vis[node] = True
        recStack[node] = True

        for j in adjList[node]:
            if not vis[j]:
               if dfs(j):
                   return True
            elif recStack[j]:
                return True

        recStack[node] = False
        return False

    for i in range(n):
        if not vis[i]:
            if dfs(i):
                return True
    return False

if __name__ == "__main__":
    print(isCycle([[0,1],[1,2],[2,3],[3,0]], 4, 4))
