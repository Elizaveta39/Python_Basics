# The task is to get matrix a and matrix c, multiply it (matrix a * matrix b)
# You will get n and m — the number of rows and columns in the matrix a
# then the elements of the matrix a - rows with numbers separated by a space
# empty row, then m and k — the number of rows and columns in the matrix b
# then the elements of the matrix a - rows with numbers separated by a space

# reading size of matrix a
n, m = [int(i) for i in input().split()]

matrix_a = []
matrix_b = []
matrix_mult = []

# reading matrix a
for i in range(n):
    element = [int(num) for num in input().split()]
    matrix_a.append(element)

# reading row with space
space = input()

# reading size of matrix b
m, k = [int(i) for i in input().split()]

# reading matrix b
for i in range(m):
    element = [int(num) for num in input().split()]
    matrix_b.append(element)

# set element (counter) for matrix c
x = 0

# calculating matrix c
for i in range(n):  # range rows of matrix c
    matrix_mult.append([])  # add rows into matrix c
    for j in range(k):  # range columns of matrix c
        x = 0   # reset the counter
        for c in range(m):  # range of columns in matrix a and range of rows in matrix b
            x += matrix_a[i][c] * matrix_b[c][j]    # multiplying elements
        matrix_mult[i].append(x)    # add elements into matrix c

# printing matrix c
for row in matrix_mult:
    print(*row)