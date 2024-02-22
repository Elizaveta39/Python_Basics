# The task is to swap the columns of the matrix, according to the entered column indexes
# You will get n and m — the number of rows and columns in the matrix,
# then the elements of the matrix - rows with numbers separated by a space
# then a line (columns indexes) with 2 numbers in it separated by a space

n = int(input())
m = int(input())
mult = []

# reading the matrix

for i in range(n):
    element = [int(num) for num in input().split()]
    mult.append(element)

# reading and preparing the columns indexes

line = input().split()
i, j = int(line[0]), int(line[1])

# swapping the columns while printing the matrix

for r in range(n):
    for c in range(m):
        if c == i:
            print(mult[r][j], end=" ")
        elif c == j:
            print(mult[r][i], end=" ")
        else:
            print(mult[r][c], end=" ")
    print()