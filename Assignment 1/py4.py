KM=int(input("Enter the no. of KM travelled:"))
r=0
if(KM>=0 and KM<=10):

    print("the total price: 80")
elif(KM>=11 and KM<=20):
    r=(KM-10)*6+80
    print(f"The total chrage{r}")
elif(KM>=21 and KM<=30):
    r=(KM-20)*5+ 80
    print(f"The total chrage{r}")
elif(KM>=31):
    r=(KM-30)*3+80
    print(f"The total chrage{r}")
else:
    print("enter valid km")