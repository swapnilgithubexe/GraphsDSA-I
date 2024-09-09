def isCyclePresentDFS(i, parent, arr, vis):
    vis[i] = True
    for v in arr[i]:
        if not vis[v]:
            if isCyclePresentDFS(v, i, arr, vis):
                return True
        elif v != parent:
            return True
    return False

def cycleDetection(edges,n,m):
    vis = [False for _ in range(n)]
    adjList = [[] for _ in range(n)]

    for u, v in edges:
        adjList[u-1].append(v-1)
        adjList[v-1].append(u-1)

    for i in range(n):
        if not vis[i]:
            ans = isCyclePresentDFS(i, -1, adjList, vis)
            if ans:
                return True

    return False

if __name__ == "__main__":
    print(cycleDetection([[3, 2], [1, 2]], 3,2))
