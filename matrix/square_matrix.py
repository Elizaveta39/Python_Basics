# You need to find the trace of the square matrix (the sum of the elements of the main diagonal)
# You will get n — the number of rows and columns in the matrix
# and then the elements of the matrix - rows with numbers separated by a space

n = int(input())    # 3
matrix = []
total = 0

# reading the square matrix

for i in range(n):
    element = [int(num) for num in input().split()] # num = "1 2 3", "4 5 6", "7 8 9"
    matrix.append(element)

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# calculating the matrix trace

for k in range(n):
    total += int(matrix[k][k])

print(total)