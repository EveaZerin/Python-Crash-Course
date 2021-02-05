def even_numbers(maximum):
	if maximum==1 or maximum==0:
		return "No numbers displayed"
	
	return_string = ""
	for x in range(2,maximum+1,2):
		if x%2==0:
			return_string += str(x) + " "
		
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

#######################################################################
def loop(start, stop, step):
	return_string = ""
	if step == 0:
		if(start<stop):
		  for x in range(start, stop, 1):
		    return_string+=str(x)+" "
		else:
		  for x in range(start, stop, -1):
		    return_string+=str(x)+" "
		return return_string
		
	if start>stop and step!=0 :
		step = abs(step) * -1
	else:
		step = abs(step)
	for count in range(start, stop, step):
		return_string += str(count) + " "
	return return_string.strip()

print(loop(11,2,3)) # Should be 11 8 5
print(loop(1,5,0)) # Should be 1 2 3 4
print(loop(-1,-2,0)) # Should be -1
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24 
print(loop(1,1,1)) # Should be empty
