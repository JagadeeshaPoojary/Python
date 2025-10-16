a =int(input("Enter first int num:"))
b=int(input("enter second int Num:"))

choice = int(input("Enter ur Choice:1-Add, 2-Sub, 3-Mul,4-Div"))
if(choice==1):
    res=a+b
    print(f"Sum of {a} and {b} is {res}")
elif(choice==2):
    res=a-b
    print(f"sub of {a} and {b} is {res}")

elif(choice==3):
    res=a*b
    print(f"mul of {a} and {b} is {res}")

elif(choice==4):
    res=a/b
    print(f"sub of {a} and {b} is {res}")
else:
    print(f"Invalid Choice, try again")
