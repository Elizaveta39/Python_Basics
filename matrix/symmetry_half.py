# The task is to swap elements symmetrically with respect to the horizontal (upper lists with lower ones)
# You will get n — the number of rows and columns in the matrix
# and then the elements of the matrix - rows with numbers separated by a space

n = int(input())
matrix = []

# reading the square matrix

for i in range(n):
    element = [int(num) for num in input().split()]
    matrix.append(element)

# swapping the lists

for j in range(n // 2):
    matrix[j], matrix[-(j + 1)] = matrix[-(j + 1)], matrix[j]

# printing the matrix

for row in matrix:
    print(*row)