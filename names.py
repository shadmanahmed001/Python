students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# this is a list of dicts
# # for data, value in students[0]:
# i = 0
# # for elements in students:
# for data, value in students[i]:
# 	dict.values(students[i])
# 	print values


def names(students):
	for item in students:
		print item['first_name']+ ' ' +item['last_name']
		
names(students)

