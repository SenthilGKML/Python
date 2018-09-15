# Storing dictionaries in a list

# Create a empty list

students = []

# Create students details in dictionary and add it in list

student ={
		  'last_name':'Ganapathy',
		  'first_name':'Senthilkumar',
		  'standard':'12th standard F Section'
		  }

students.append(student)
student ={
		  'last_name':'Senthil',
		  'first_name':'Sriyaa',
		  'standard':'1st standard F Section'
		  }
		  
		  

students.append(student)

# Show all students info thro loop

for student_dic in students:
	for f_name, l_name in student_dic.items():
		print(f_name+l_name)
	print("\n")
