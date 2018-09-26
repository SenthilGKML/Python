file = open("fruits.txt", "r")
content = file.readlines()
file.close()
for i in content:
     print(len(i) - 1)
	 
file=open("fruits.txt",'r')
content=file.readlines()
content=[i.rstrip("\n") for i in content]
for x in content:
	print(len(x))
file.close()
	 