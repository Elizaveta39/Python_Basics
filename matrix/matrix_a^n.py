# The task is to raise the matrix to the power of m
# you will get n - size of square matrix
# then the elements of the matrix a - rows with numbers separated by a space
# m - the power to which the matrix needs to be raised

n = int(input())
matrix_a = []
matrix_c = []   # final matrix
for _ in range(n):
    element = [int(num) for num in input().split()]
    matrix_a.append(element)
    matrix_c.append(element)  # create copy of matrix_a

m = int(input())

# calculating matrix c
for _ in range(m - 1):  # do m - 1 multiplications
    temp_matrix = [[0] * n for _ in range(n)]  # create temporary matrix to save midterm results
    for i in range(n):    # range rows of matrix c
        for j in range(n):    # range columns of matrix c
            for c in range(n):    # range of columns in matrix c and range of rows in matrix a
                temp_matrix[i][j] += matrix_c[i][c] * matrix_a[c][j]    # multiplying elements
    matrix_c = temp_matrix  # renew matrix_c

# printing results
for row in matrix_c:
    print(*row)