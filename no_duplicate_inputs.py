i=1
dict1 = {}
while i<=10:
  n = int(input("Enter a number"))
  if n in dict1.values():
    print("Duplicate found")
  else:
    dict1[i]=n
    i+=1

print(dict1)      
