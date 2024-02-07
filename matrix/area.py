# The task is to find the largest number among the numbers below the main diagonal of the matrix
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

# Compare numbers below the main diagonal with maxim
# We also need to compare the numbers located in the main diagonal of the matrix
# (j = k) - numbers in the main diagonal
# (j > k) - numbers below the main diagonal

for j in range(n):
    for k in range(n):
        if j >= k and matrix[j][k] > maxim:
            maxim = matrix[j][k]

print(maxim)

