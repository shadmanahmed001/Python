attempt = 0
heads = 0
tails = 0
for attempt in range(0,5000):
	print 'Starting the program'
	import random
	x = random.random()
	x_rounded= round(x)
	if x_rounded == 0:
		heads= heads + 1
		attempt+= 1
		print "Attempt#" +str(attempt)+ ": Throwing a coin.... It's a head! ... Got " +str(heads)+ " head(s) so far and"+ str(tails)+"tail(s) so far"
	if x_rounded == 1:
		tails= tails + 1
		attempt+= 1
		print "Attempt#", str(attempt), ": Throwing a coin.... It's a tail! ... Got ",str(heads)," head(s) so far and", str(tails), "tail(s) so far"

