# Task: Write a program that reads the elements of the matrix one by one,
# outputs them as a matrix, outputs an empty row, and again the same matrix,
# but already swapping rows with columns: the first row is output as the first column, and so on.


rows, columns = int(input()), int(input())  # rows = 4, columns = 2
matrix = []

# reading the matrix

for i in range(rows):
    matrix.append([])
    for j in range(columns):
        matrix[i].append(str(input()))

# matrix = [["a", "b"],
#           ["c", "d"],
#           ["e", "f"],
#           ["g", "h"]]

# printing the matrix

for r in range(rows):
    for c in range(columns):
        print(matrix[r][c], end=" ")
    print()

# the following output will be printed:
# a b
# c d
# e f
# g h

print()

# printing the matrix in reverse order

for col in range(columns):  # 2
    for row in range(rows): # 4
        print(matrix[row][col], end=" ")
    print()

# the following output will be printed:
# a c e g
# b d f h