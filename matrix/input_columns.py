# The task is to print a matrix filled with numbers from 1 to m * n
# in such order: 1st column from up to down, 2nd from up to down, etc...
# You will get n and m — the number of rows and columns in the matrix

n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

elem = 1    # variable for values in matrix

for i in range(m):
    for j in range(n):  # filling the matrix with numbers from 1 to m * n
        matrix[j][i] = elem
        elem += 1

# printing the matrix in correct order
for row in range(n):
    for col in range(m):
        print(str(matrix[row][col]).ljust(3), end=" ")
    print()