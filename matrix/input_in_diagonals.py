# The task is to fill the matrix with elements from 0 to n * m inclusive by diagonals
# example: elem[0][0] -> elem[0][1], elem[1][0] -> elem[0][2], elem[1][1], elem[2][0] ...
# you'll get n and m in one string separated by a space

# Reading n and m
n, m = [int(i) for i in input().split()]

# Filling matrix with 0
matrix = [["0"] * m for _ in range(n)]

# Starting to create elements with 1st one
elem = 1

# Creating nested loop with 3 levels:
# 1st level - sums i + j (elements in each diagonal have equal sums of its indexes)
# range(n + m - 1) - the range of all possible element indexes sums of the matrix
# level 2nd and 3rd - for element's indexes, we need to check their sums to be equal to q
# if find it, change 0 to elem and increase elem by 1 (elem += 1)
for q in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                matrix[i][j] = elem
                elem += 1

# printing the matrix
for row in matrix:
    print(*row)