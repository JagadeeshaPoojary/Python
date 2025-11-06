marks={}.fromkeys(['python','java','web'],100)
print("Dictionary mark is :",marks)

print("*****************************************************************************")
for i in marks.items():
    print(i)

print("******************************************************************************")
print("Key are:",marks.keys())
print("Values are:",marks.values())


print("Sorted :",sorted(marks))
print("Sorted eith reverse:",sorted(marks,reverse=True))

print("************************************************")
print("Sorted items:",sorted(marks.items()))
print("Sorted items with reverse ",sorted(marks.items(),reverse=True))