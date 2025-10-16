BikePrice=int(input("Enter the cost of bike:"))
if(BikePrice>100000):
    print("RoadTax:15%")
elif(BikePrice>50000 and BikePrice<=100000):
    print("RoadTax:10%")
elif(BikePrice<=50000):
    print("RoadTax:5%")
else:
    print("Invalid Input")