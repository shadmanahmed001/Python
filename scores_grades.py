
a = [87,67,95,100,75,90,89,72,60,98]
def scores_grades(a):
	for element in a:
		if element >=60 and element <=69:
			print 'Score: '+str(element)+'; Your grade is D'
		elif element >=70 and element <=79:
			print 'Score: '+str(element)+'; Your grade is C'
		elif element >=80 and element <=89:
			print 'Score: '+str(element)+'; Your grade is B'
		elif element >=90 and element <=100:
			print 'Score: '+str(element)+'; Your grade is A'	
print scores_grades(a)




	