# The task is to find the indexes (row and column) of the first occurrence of the maximum element
# You will get n and m — the number of rows and columns in the matrix
# and then the elements of the matrix - rows with numbers separated by a space

n = int(input())
m = int(input())
mult = []

# reading the matrix

for i in range(n):
    element = [int(num) for num in input().split()]
    mult.append(element)

# finding the maximum element in the matrix and its indexes

row, col = 0, 0

for i in range(n):
    for j in range(m):
        if mult[i][j] > mult[row][col]: # comparing each element with the 1st one and if finding a bigger one,
            # compare the rest with this one
            row, col = i, j

print(row, col)