Age=int (input("Enter the Person Age:"))
Gender=input("Enter the gender of the person(M/F):").upper()
Days=int(input("Enter the number of days:"))
wages_per_Day=0
if(Age>=18 and Age<30):
    if(Gender== 'M'):
        print("Number of wages per day is 700")
        wages_per_Day=700
    elif(Gender== 'F'):
        print("Number of wages per day is 750")
        wages_per_Day=750
elif(Age >= 30 and Age<40):
    if(Gender == 'M'):
        print("Number of wages per day is 800")
        wages_per_Day=800
    elif(Gender== 'F'):
        print("Number of wages per day is 850")
        wages_per_Day=850
else:
    print("Enter the valid age")
if(wages_per_Day>0):
    Total_wages=wages_per_Day*Days
print(f"Wages per day:{wages_per_Day}")
print(f"Total wages per {Days} is {Total_wages}")