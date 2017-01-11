a = [2,4,10,16]
def multiply(a,x):
	i =0
	for element in a:
		a[i]= a[i] * x
		i =i + 1
	print a
multiply(a, 5)
