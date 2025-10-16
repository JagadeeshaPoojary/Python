mark= int(input("Enter the marks "))
if(mark>=81 and mark<=100):
    print("Grade is A ")
elif(mark>=71 and mark<=80):
    print("Grade is B ")
elif(mark>=61 and mark<=70):
    print("Grade is C ")

elif(mark>=50 and mark<=60):
    print("Grade is D ")
elif(mark>=0 and mark<=49):
    print("Fail ")
else:
    print("Invalid Marks")