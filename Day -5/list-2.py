product_name=[]
product_price=[]
sum=0;

while(True):
    option =  int(input("Option-1:Enter product details   2- Exit: " ))

    if(option == 1):
     name=input("Enter the product name :")
     product_name.append(name)
     price = input("Enter the price of the product: ")
     product_price.append(price)

    elif(option == 2):
       break

    else:
       print("Invalid option")

print("******************** Cart Details ***********************")

for i in range(len(product_name)):
   print(product_name[i], "------------>", product_price[i])

total=sum(product_price)
print("The total cost of all the product is",total)