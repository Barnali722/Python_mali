# Define the two 3x3 matrices as lists of lists 
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Initialize a result matrix with zeros 
C = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Perform matrix multiplication using nested loops 
for i in range(len(A)):  # Iterate through rows of A 
    for j in range(len(B[0])):  # Iterate through columns of B 
        for k in range(len(B)):  # Iterate through elements of the row of A and column of B

            C[i][j] += A[i][k] * B[k][j]

# Print the result 
print("Matrix A:")
for row in A:
    print(row)
print("\nMatrix B:")
for row in B:
    print(row)
print("\nResult using nested loops:")
for row in C:
    print(row)