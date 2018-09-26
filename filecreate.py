""" This is test for documentation steps in Python """
temperatures=[10,-20,-289,100]

def writer(t):
	with open("exam1.txt","w") as file:
		for x in t:
			if x>-273.15:
				f=x*9/5+32
				file.write(str(x)+"\n")
				
writer(temperatures)