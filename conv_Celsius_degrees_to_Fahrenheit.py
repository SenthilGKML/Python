def  conv_Celsius_degrees_to_Fahrenheit(c):
	if c < -273:
		print("Please pass the valid")
	else:
		F = c * 9/5 + 32
		print(F)

	
conv_Celsius_degrees_to_Fahrenheit(float(input("value to calculate fahrenheit")))	