def odd_even(i):
	x = 0
	while x < i:
		if x % 2 == 0:
			print 'Number is '+ str(x)+ '. This is an even number.'
			x = x+1
		elif x % 2 == 1:
			print 'Number is '+ str(x)+ '. This is an odd number.'
			x = x+1
odd_even(2000)	
print 'its done!'