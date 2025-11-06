a=[[0,0],[0,0]]
b=[[0,0],[0,0]]
c=[[0,0],[0,0]]

print("Enter Matrix A element:")
for i in range(2):
    for j in range(2):
        a[i][j]=input("Enter an element to the  list:")
print("Enter Matrix B element:")
for i in range(2):
    for j in range(2):
        b[i][j]=input("Enter an element to the  list:")
print("Enter Matrix C element:")
for i in range(2):
    for j in range(2):
        c[i][j]=input("Enter an element to the  list:")
print("List A is: ")
for i in range (2):
    for j  in range (2):
        print(a[i][j], end="\t")
    print()
print("List B is: ")
for i in range (2):
    for j  in range (2):
        print(b[i][j], end="\t")
    print()
print("List C is: ")
for i in range (2):
    for j  in range (2):
        print(c[i][j], end="\t")
    print()