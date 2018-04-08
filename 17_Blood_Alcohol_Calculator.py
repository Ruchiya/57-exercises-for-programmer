
while True :
	try:
		W = float(input("What is your weight in pound:"))
		r = input("What is your gender? 'female' or 'male':").lower()
		A = float(input("The amount of alcohol by volume of the drinks consumed in ounces:"))
		H = float(input("The number of hour since last drink:"))
		break
	except ValueError:
		print("Try again")


if r == 'female' or r == 'f':
	r = 0.66
else:
	r = 0.73

BAC= round(((A * 5.14)/(W/r))- (0.15*H),2)

if BAC >=0.08:
	print(f"Your BAC is {BAC},It is not legal for you to drive")
else:
	pring(f"Your BAC is {BAC},You can drive, but stay safe")
