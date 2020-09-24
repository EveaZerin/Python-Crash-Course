dict1 = {'a': 100, 'b': 100, 'c': 200, 'd': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400, 'e': 200}
dict3 = {}

for key in dict1.keys():
  if key in dict2.keys():
    dict3[key]=dict1[key]+dict2[key]
  else:
    dict3[key]=dict1[key]

for key in dict2.keys():
  if key not in dict1.keys():
    dict3[key]=dict2[key]    

print(dict3) 
