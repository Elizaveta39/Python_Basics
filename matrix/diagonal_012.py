# The task is to print a matrix filled with 1s on the side diagonal,
# 2s under the side diagonal and 0s above the side diagonal
# You will get n — the number of rows and columns in the matrix

n = int(input())

matrix = [["2"] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][n - i - 1] = "1"
        if i < n - 1 - j:
            matrix[i][j] = "0"

# printing matrix
for row in matrix:
    print(*row)
