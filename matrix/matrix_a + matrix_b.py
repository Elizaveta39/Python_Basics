# The task is to get matrix a and matrix c, show the sum of them - matrix c
# You will get n and m — the number of rows and columns in the matrix
# then the elements of the matrix a - rows with numbers separated by a space, empty row, elements of the matrix b

n, m = [int(i) for i in input().split()]
matrix_a = []
matrix_b = []
matrix_sum = []

# reading matrix a
for i in range(n):
    element = [int(num) for num in input().split()]
    matrix_a.append(element)

# reading row with space
space = input()

# reading matrix b
for i in range(n):
    element = [int(num) for num in input().split()]
    matrix_b.append(element)

# calculating sum of matrix a and b
for i in range(n):
    matrix_sum.append([])
    for j in range(m):
        matrix_sum[i].append(matrix_a[i][j] + matrix_b[i][j])

# printing matrix c
for row in matrix_sum:
    print(*row)