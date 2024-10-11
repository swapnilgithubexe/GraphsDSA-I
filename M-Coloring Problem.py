def isSafe(mat, node, color, col_arr, n):
    for i in range(n):
        if mat[node][i] == 1 and col_arr[i] == color:
            return False

    return True

def solve(node, mat, col_arr, n, m):
    if node == n:
        return True

    for color in range(1, m+1):
        if isSafe(mat, node, color, col_arr, n):
            col_arr[node] = color

            if solve(node + 1, mat, col_arr, n, m):
                return True

            col_arr[node] = 0

    return False



def coloringproblem(adjmat, n, m):
    color_array = [0 for _ in range(n)]
    if solve(0, adjmat, color_array, n, m):
        return True
    return False

if __name__ == "__main__":
    # Test case 1: Simple graph (2-colorable)
    adjMatrix1 = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    n1 = 4  # Number of nodes
    m1 = 2  # Number of colors
    print(coloringproblem(adjMatrix1, n1, m1))  # Expected output: True (graph is 2-colorable)

    # Test case 2: Simple graph (not 2-colorable)
    adjMatrix2 = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    n2 = 4  # Number of nodes
    m2 = 2  # Number of colors
    print(coloringproblem(adjMatrix2, n2, m2))  # Expected output: False (graph is not 2-colorable)

    # Test case 3: 3-colorable graph
    adjMatrix3 = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    n3 = 4  # Number of nodes
    m3 = 3  # Number of colors
    print(coloringproblem(adjMatrix3, n3, m3))  # Expected output: True (graph is 3-colorable)

    # Test case 4: Complete graph (requires 4 colors)
    adjMatrix4 = [
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0]
    ]
    n4 = 4  # Number of nodes
    m4 = 3  # Number of colors
    print(coloringproblem(adjMatrix4, n4, m4))  # Expected output: False (complete graph requires 4 colors)

    # Test case 5: Complete graph with enough colors (4-colorable)
    m5 = 4  # Number of colors
    print(coloringproblem(adjMatrix4, n4, m5))  # Expected output: True (graph is 4-colorable)
