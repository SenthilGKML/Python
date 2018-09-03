#Adding Dictionaries directly in list without using append

books_dic_list = [
			{
			'book1':'who will cry when you die',
			'author':'Robin Sharma',
			},
			{
			'book2':'The Monk who sold his Ferrari',
			'author':'Robin Sharma',
			},
		
    ]

# show all info about each book

for book_dic in books_dic_list :
	for k, v in book_dic.items():
		print(k +":" +v)
	print("\n")