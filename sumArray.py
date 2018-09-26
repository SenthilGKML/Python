import sys

def simpleArraySum(n, ar):
    # Complete this function
	for a in ar:
		if a > n:
			result=+ar
			

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)