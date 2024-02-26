# The task is to swap the elements of the main and side diagonal
# so that the upper element of the main diagonal takes the place of the lower element of the side diagonal
# You will get n — the number of rows and columns in the matrix
# and then the elements of the matrix - rows with numbers separated by a space

n = int(input())
matrix = []

# reading the square matrix

for i in range(n):
    element = [int(num) for num in input().split()]
    matrix.append(element)

# exchanging elements in the diagonals
# elements of the side diagonal are read from right to left and are located with such indexes matrix[i][n - i - 1]
# to meet the conditions of the task, you need to take elements with such indexes matrix[n - i - 1][i]

for j in range(n):
    matrix[j][j], matrix[n - j - 1][j] = matrix[n - j - 1][j], matrix[j][j]

# printing the matrix

for row in matrix:
    print(*row)