import heapq


def isSafe(row, col, visited, mat, n, m):
    # Ensure the cell is within the matrix boundaries, hasn't been visited, and is not blocked
    if 0 <= row < n and 0 <= col < m and not visited[row][col] and mat[row][col] == 1:
        return True
    return False


def shortestPathInMaze(matrix, src, dest):
    if src == dest and matrix[src[0]][src[1]] != 0:
        return 0
    if matrix[src[0]][src[1]] == 0:
        return -1

    n = len(matrix)  # Number of rows
    m = len(matrix[0])  # Number of columns

    # Initialize the minimum cost matrix with infinity for all cells
    min_cost = [[float("inf") for _ in range(m)] for _ in range(n)]
    # Initialize the visited matrix to keep track of visited nodes
    visited = [[False for _ in range(m)] for _ in range(n)]

    # Min-heap to store (cost, (row, col)) and always pop the smallest cost node
    heap = []
    heapq.heappush(heap, (0, src))  # Push the source node with cost 0
    min_cost[src[0]][src[1]] = 0

    # Define the 4 possible movement directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Dijkstra's Algorithm loop
    while heap:
        top_element = heapq.heappop(heap)  # Get the cell with the smallest cost
        cost, node = top_element
        row, col = node  # Decompose the node into row and col

        # If the current node has already been visited, skip it
        if visited[row][col]:
            continue

        # Mark the node as visited
        visited[row][col] = True

        # Check all possible 4 directions
        for d in directions:
            new_row = d[0] + row
            new_col = d[1] + col

            # If the new cell is valid and not visited
            if isSafe(new_row, new_col, visited, matrix, n, m):
                new_cost = cost + 1
                # If the new cost is smaller, update the cost and push to heap
                if new_cost < min_cost[new_row][new_col]:
                    min_cost[new_row][new_col] = new_cost
                    heapq.heappush(heap, (new_cost, (new_row, new_col)))

    # If destination was never reached, return -1
    if min_cost[dest[0]][dest[1]] == float("inf"):
        return -1

    # Return the minimum cost to reach the destination
    return min_cost[dest[0]][dest[1]]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple case with an open path
    matrix1 = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ]
    src1 = (0, 0)
    dest1 = (2, 2)
    print(shortestPathInMaze(matrix1, src1, dest1))  # Expected: 4

    # Test Case 2: No path available (blocked)
    matrix2 = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    src2 = (0, 0)
    dest2 = (2, 2)
    print(shortestPathInMaze(matrix2, src2, dest2))  # Expected: -1

    # Test Case 3: Destination is source
    matrix3 = [
        [1, 1],
        [1, 1]
    ]
    src3 = (0, 0)
    dest3 = (0, 0)
    print(shortestPathInMaze(matrix3, src3, dest3))  # Expected: 0

    # Test Case 4: Larger matrix with a valid path
    matrix4 = [
        [1, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 1, 1],
        [0, 1, 0, 1]
    ]
    src4 = (0, 0)
    dest4 = (3, 3)
    print(shortestPathInMaze(matrix4, src4, dest4))  # Expected: 5

    # Test Case 5: Matrix where destination is blocked
    matrix5 = [
        [1, 1],
        [1, 0]
    ]
    src5 = (0, 0)
    dest5 = (1, 1)
    print(shortestPathInMaze(matrix5, src5, dest5))  # Expected: -1