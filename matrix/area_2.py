# The task is to find the largest number in the right and left quarters of the square matrix
# You will get n — the number of rows and columns in the matrix
# and then the elements of the matrix - rows with numbers separated by a space


n = int(input())
matrix = []

# reading the square matrix

for i in range(n):
    element = [int(num) for num in input().split()]
    matrix.append(element)

# Setting the 1st number of the 1st row of the matrix as the largest number

maxim = matrix[0][0]

# Compare numbers in the right and left quarters with maxim
# We also need to compare the numbers located in the diagonals of the matrix
# (i >= j and i + j + 1 <= n) - numbers in left quarter and in the main diagonal
# (i <= j and i + j + 1 >= n) - numbers in right quarter and in the side diagonal

for i in range(n):
    for j in range(n):
        if (i >= j and i + j + 1 <= n) or (i <= j and i + j + 1 >= n):
            maxim = matrix[i][j]

print(maxim)