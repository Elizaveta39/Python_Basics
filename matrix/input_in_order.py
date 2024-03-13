# The task is to print a matrix in such order,
# so 1st column would be filled with numbers from 1 to m
# and the rest numbers in rows would be from 1st number in the ro to m and then starts from n to m
# You will get n and m — the number of rows and columns in the matrix

n, m = [int(i) for i in input().split()]
matrix = []

elem = 0    # variable for values in 1st column
elem_2 = 0  # variable for values in rows

for i in range(n):  # counting and adding numer to 1st column
    elem += 1
    if elem > m:    # if elem > m, starting it from 1
        elem = 1
    matrix.append([elem])
    elem_2 = elem + 1
    for j in range(m - 1):  # counting and adding numer to the rows
        if elem_2 <= m:
            matrix[i].append(elem_2)
        else:   # if elem_2 > m, starting it from 1
            elem_2 = 1
            matrix[i].append(elem_2)
        elem_2 += 1

# print matrix
for row in matrix:
    print(*row)
