CustomerName=(input("Enter the customer name:"))
CustomerID=input("Enter theb customer ID:")
Units=float(input("Enter the number of units consumed by the user:"))
charge=0

print("-----------Electricty Bill--------------")
if(Units<=100):
    charge=Units*0
    print("Bill amount is Zero")
elif(Units>100 and Units<=200):
    charge=(Units-100)*5
    print(f"Customer name:{CustomerName}") 
    print(f" Customer ID:{CustomerID}")
    print(f"Consumed Units: {Units}")
    print(f"Total amount: {charge}")
else:
    charge=(Units-200)*10
    print(f"Customer name:{CustomerName}") 
    print(f" Customer ID:{CustomerID}")
    print(f"Consumed Units: {Units}")
    print(f"Total amount: {charge}")

