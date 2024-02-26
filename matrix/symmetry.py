# The task is to print YES if the matrix is symmetric and NO if it is not symmetric
# symmetrical means that the elements below the main diagonal are equal to the elements above
# You will get n — the number of rows and columns in the matrix
# and then the elements of the matrix - rows with numbers separated by a space

n = int(input())
matrix = []

# reading the square matrix

for i in range(n):
    element = [int(num) for num in input().split()]
    matrix.append(element)

# setting the flag to false to stop the double loop
# stopping loop at the first mismatch
# if break works, we print NO
# if loop finishes without break, than else works printing YES

found = False
for i in range(n):
    if found:
        break
    for j in range(n):
        if i != j and matrix[i][j] != matrix[j][i]:
            print("NO")
            found = True
            break
else:
    print("YES")