#Challenge Included 

legal = {
16:'United State,Canada',
17:'Philippines, Guyana',
18:'China, Japan, South Korea, Egypt,Morocco'}

while True:
	try:
		age = int(input("What is your age:"))
		if age <=0:
			raise ValueError
		if age >= age in legal:
			country = [v for k,v in legal.items() if k <=age]
			print('You are old enough to legally drive in : {}'.format(country))
		else:
			print("You are not old enough to legally drive")
		break
	except ValueError:
		print("Not a valid age")
