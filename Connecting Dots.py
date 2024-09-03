# Problem statement
# Gary has a board of size NxM. Each cell in the board is a coloured dot. There exist only 26 colours denoted by uppercase Latin characters (i.e. A,B,...,Z). Now Gary is getting bored and wants to play a game. The key of this game is to find a cycle that contain dots of same colour. Formally, we call a sequence of dots d1, d2, ..., dk a cycle if and only if it meets the following condition:
#
# 1. These k dots are different: if i≠j then di is different from dj.
# 2. k is at least 4.
# 3. All dots belong to the same colour.
# 4. For all 1≤i≤k-1: di and di+1 are adjacent. Also, dk and d1 should also be adjacent. Cells x and y are called adjacent if they share an edge.
# Since Gary is colour blind, he wants your help. Your task is to determine if there exists a cycle on the board.

import sys
sys.setrecursionlimit(10000)


def isSafe(x, y, n,m):
    return 0 <= x < n and 0 <= y < m


def dfs(arr, x, y, n,m, parentx, parenty, color, visited, path_length):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    visited[x][y] = True

    for dx, dy in directions:
        newx, newy = x + dx, y + dy
        if isSafe(newx, newy, n, m) and arr[newx][newy] == color:
            if not visited[newx][newy]:
                if dfs(arr, newx, newy, n,m, x,y,color, visited, path_length + 1):
                    return True
            elif newx != parentx or newy != parenty:
                if path_length >= 4:
                    return True
    return False


def connectingDots(arr, n, m):
    if n == 0 or m == 0:
        return False

    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if dfs(arr, i, j, n,m, -1, -1, arr[i][j], visited, 1):
                return True

    return False

if __name__ == "__main__":
    print(connectingDots([
        ['A', 'A', 'A', 'A', 'A', 'B'],
        ['A', 'B', 'B', 'B', 'A', 'B'],
        ['A', 'B', 'A', 'A', 'A', 'B'],
        ['A', 'B', 'A', 'B', 'B', 'B'],
        ['A', 'B', 'A', 'A', 'A', 'B'],
        ['A', 'B', 'B', 'B', 'A', 'B'],
        ['A', 'A', 'A', 'A', 'A', 'B']
    ], 7, 6))

    print("-------------------")
    print(connectingDots([['A','A'], ['A', 'B']], 2,2))