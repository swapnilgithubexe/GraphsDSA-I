def isSafe(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def dfs(arr, s, x, y, n, m, index, visited):
    if index == len(s):
        return True

    visited[x][y] = True
    directions = [(-1,0), (0,-1), (1,0),(0,1),(1,1),(-1,-1), (-1, 1), (1, -1)]

    for dx, dy in directions:
        newx, newy = x + dx, y + dy
        if isSafe(newx, newy, n, m) and not visited[newx][newy] and arr[newx][newy] == s[index]:
            if dfs(arr, s, newx, newy, n, m, index+1, visited):
                return True

    return False




def checkword(arr, n, m):
    s = "CODINGNINJA"
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if arr[i][j] == s[0]:
                if dfs(arr, s, i, j, n, m, 1, visited):
                    return "Yes the word is present."

    return "Oops no word found"

if __name__ == "__main__":
    print(checkword([
  ['C', 'A', 'N', 'I'],
  ['O', 'O', 'J', 'N'],
  ['D', 'D', 'I', 'G'],
  ['J', 'N', 'I', 'N']
], 4,4))
    print("-----------------------")
    print(checkword([
  ['D', 'A', 'N', 'D', 'O'],
  ['N', 'N', 'I', 'N', 'J'],
  ['A', 'X', 'G', 'J', 'C'],
  ['I', 'N', 'J', 'A', 'A'],
  ['C', 'O', 'D', 'D', 'I']
], 5, 5))