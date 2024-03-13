# The task is to print a matrix in spiral order,
# You will get n and m — the number of rows and columns in the matrix
# You have to fill matrix with numbers from 1 to n * m


n, m = [int(i) for i in input().split()]

matrix = [["0"] * m for _ in range(n)]

elem = 1  # a variable to fill in the values in the matrix
row, col = 0, 0  # indexes of the current row and column
dr, dc = 0, 1  # direction of movement on the matrix: to the right

# go through the matrix and fill it with values from 1 to n * m
for _ in range(n * m):
    matrix[row][col] = elem  # setting the value in the current position
    elem += 1  # increasing the value for the next position

    # check whether we have reached the border or met an already visited cell
    if 0 <= row + dr < n and 0 <= col + dc < m and matrix[row + dr][col + dc] == 0:
        # moving on to the next cell
        row += dr
        col += dc
    else:
        # changing the direction of movement in a spiral
        dr, dc = dc, -dr
        row, col = row + dr, col + dc

# print matrix
for row in matrix:
    print(*row)
