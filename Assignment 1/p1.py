    eid=int(input("Enter Employee id:"))
    name = input("Enter Employee nmame:")
    designaton=input("Enter Employee designaton:=")
    basic=float(input("Enter Basic salary"))
    da=basic*0.50
    hra=basic*0.35
    ta=basic*0.25
    gross_sal=basic+da+hra+ta
    print("--------------Employee Salary Details---------")