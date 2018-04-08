while True:
	try:
		weight = float(input("What is your weight in pounds:"))
		height = float(input("What is your height in inches:"))
		break
	except ValueError:
		print("Not numeric value, try again")


bmi  = round((weight/(height *height))*703,1)

if bmi>= 18.5 and bmi<=25:
	print(f'Your bmi is {bmi}\nYour are within the ideal weight rance')
elif bmi > 25:
	print(f'Your bmi is {bmi}\nYour are overweight')
else:
	print(f'Your bmi is {bmi}\nYou are underweight')