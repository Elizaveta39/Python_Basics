# The task is to print out a matrix of dots ".",
# fill the knight's place with a sign "N", and his possible moves with a sign "*"
# you will get the coordinates of the knight in chess notation (for example, b6)

# reading knight's coordinates in chess notation
place = str(input())

# creating matrix 8x8 filled with .
matrix = [["."] * 8 for _ in range(8)]

# converting coordinates into matrix indexes

numbers = ["8", "7", "6", "5", "4", "3", "2", "1"]  # list of numbers in reversed order (for i in matrix)
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]  # list of letters (for j in matrix)

x, y = numbers.index(place[1]), letters.index(place[0])  # indexes of N on the chess board

# inserting sign "N" for knight's coordinates

matrix[x][y] = "N"

# finding coordinates for knight's moves
# creating matrix with all possible moves

matrix_xy = [[x - 2, y - 1],
             [x - 2, y + 1],
             [x - 1, y - 2],
             [x - 1, y + 2],
             [x + 1, y - 2],
             [x + 1, y + 2],
             [x + 2, y - 1],
             [x + 2, y + 1]]

# inserting "*" in possible moves coordinates

for i in range(8):
    for j in range(1):
        k, m = matrix_xy[i][j], matrix_xy[i][j + 1]
        if 0 <= k < 8 and 0 <= m < 8:
            matrix[k][m] = "*"

# printing the matrix

for row in matrix:
    print(*row)