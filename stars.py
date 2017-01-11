x = [4, 6, 1, 3, 5, 7, 25]
for i in x:
	print '*'* i

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
for i in x:
 if type (i) is int:
 	print i* "*"
 if type (i) is str:
 	temp= i
 	y= temp.lower()
 	print y[0]* len(y)
