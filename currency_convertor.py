def currency_convertor(rate,euros):
	dollars = rate * euros;
	print(dollars)

r = input("Enter rate:")
e = input("Enter euros:")
currency_convertor(float(r),float(e))