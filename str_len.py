def str_len(abc):
	return len(abc)

val=input("Enter some String value:")

if type(val) == int:
	print("input value is not String")
else:
	print(str_len(val))
		
	
