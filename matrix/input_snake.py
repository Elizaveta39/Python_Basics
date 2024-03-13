# The task is to print a matrix in snake order (1st row as it is, next - in reverse order),
# You will get n and m — the number of rows and columns in the matrix
# You have to fill matrix with numbers from 1 to n * m

n, m = [int(i) for i in input().split()]
matrix = []

elem = 1

# filling matrix with numbers from 1 to n * m
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(elem)
        elem += 1

# if row number is an odd number, we print it in reverse
for r in range(n):
    if r % 2 == 0:
        for col in range(m):
            print(str(matrix[r][col]).ljust(3), end=" ")
    else:
        for c in range(m - 1, -1, -1):
            print(str(matrix[r][c]).ljust(3), end=" ")
    print()