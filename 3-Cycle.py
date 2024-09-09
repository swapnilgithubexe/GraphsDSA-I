def threeCycle(edges, n,m):
    adjMat = [[0] * n for _ in range(n)]

    for u, v in edges:
        adjMat[u][v] = 1
        adjMat[v][u] = 1

    count = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if adjMat[i][j] == 1 and adjMat[j][k] == 1 and adjMat[j][k] == 1:
                    count += 1

    return count

if __name__ == "__main__":
    print(threeCycle([[0,1],[0,2],[1,2],[3,4]], 6, 4))