# Initialize matrices
a = [[0, 0], [0, 0]]
b = [[0, 0], [0, 0]]
c = [[0, 0], [0, 0]]

# Input elements for Matrix A
print("Enter Matrix A elements:")
for i in range(2):
    for j in range(2):
        a[i][j] = int(input(f"Enter element A[{i}][{j}]: "))

# Input elements for Matrix B
print("Enter Matrix B elements:")
for i in range(2):
    for j in range(2):
        b[i][j] = int(input(f"Enter element B[{i}][{j}]: "))

# Add matrices
for i in range(2):
    for j in range(2):
        c[i][j] = a[i][j] + b[i][j]

# Display matrices
print("\nMatrix A:")
for i in range(2):
    for j in range(2):
        print(a[i][j], end="\t")
    print()

print("\nMatrix B:")
for i in range(2):
    for j in range(2):
        print(b[i][j], end="\t")
    print()

print("\nResultant Matrix (A + B):")
for i in range(2):
    for j in range(2):
        print(c[i][j], end="\t")
    print()
