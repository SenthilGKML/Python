arr = list(map(int, input().strip().split(' ')))
x=sum(arr)-max(arr)
y=sum(arr)-min(arr) 
print(str(x)+" "+str(y))