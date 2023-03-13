# Write a Python program which takes two digits m (row) and n (column) as input and
# generates a two-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
m= int(input("rows:"))
n= int(input("column:"))
mat= [[0 for column in range(n)]for row in range(m)]
for row in range(n):
    for column in range(m):
        mat[row][column]=row*column
print(mat)