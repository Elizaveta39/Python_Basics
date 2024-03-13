# The task is to print a matrix filled with numbers from 1 to m
# You will get n and m — the number of rows and columns in the matrix

n, m = [int(i) for i in input().split()]
matrix = []

elem = 1    # variable for values in matrix

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(elem)
        elem += 1

# printing the matrix with 3 symbols for each matrix value
for row in range(n):
    for col in range(m):
        print(str(matrix[row][col]).ljust(3), end=" ")
    print()
