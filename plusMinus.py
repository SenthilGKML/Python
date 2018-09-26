n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
b=len(arr)
o=0;
p=0;
q=0;

for a in arr:
	if a >0:
		o+=1		
	elif a < 0:
		p+=1
	elif a == 0:
		q+=1
x=o/float(b)
y=p/float(b)
z=q/float(b)
print(x)
print(y)
print(z)
	