TimePeriod=int(input("How many years employee worked in a company:"))
Salary=int(input("Enter the employee salary:"))
BS=0
if(TimePeriod>10):
    BS=Salary+(Salary/100*10)
    print("Company decide to give 10% bonus to employee")
elif(TimePeriod >=6 and TimePeriod<=10):
    BS=Salary+(Salary/100*8)
    print("Company decide to give 8% bonus to employee")
else:
        BS=Salary+(Salary/100*5)
        print("Company decide to give 5% bonus to employee")
print(f"{TimePeriod} years Employee worked in company")
print(f"Employee salary is {BS}")



