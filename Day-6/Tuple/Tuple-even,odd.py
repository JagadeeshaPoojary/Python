t1=(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Tuple t1 is :",t1)
even_list=[]
odd_list=[]
even,odd=0,0

print("-------------Even-----------")
for  i in t1:
    if(i%2==0):
        even_list.append(i)
        even+=1

print("Total even number are",even)
print(even_list)

for i in t1:
    if(i%2!=0):
        odd_list.append(i)
        odd+=1
print("Total odd numbers are:",odd)   
print(odd_list)