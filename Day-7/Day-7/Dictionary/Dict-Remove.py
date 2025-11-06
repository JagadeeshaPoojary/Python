d1={1: 2, 2: 4, 3: 9, 4:16}
print(d1)

print("pop value is:",d1.pop(2))
print("updated dictionary is:",d1)

print("pop item is:",d1.popitem())   #remove an arbitrory item, return
print("updated dictionary is:",d1)

d1.clear()
print("updated dictionary is:",d1)

del d1
