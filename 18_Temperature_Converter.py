choice = input("Press C to convert from Fahrenheit to Celsius\nor\nPress F to convert from Celsius to Fahrenheit:").lower()


def c_to_f(c):
	f = (c*9/5)+32
	print(f"The temperature in Fahrenheit is {f} F")

def f_to_c(f):
	c = (f-32)*5/9
	print(f"The temperature in Celsius is {c} C")

if choice == 'c':
	while True:
		try:
			temp = float(input('Please enter the temperature in celcius:'))
			c_to_f(temp)
			break
		except ValueError:
			print("Not a numeric value, try again")

elif choice == 'f':
	while True:
		try:
			temp = float(input('Please enter the temperature in fahrenheit:'))
			f_to_c(temp)
			break
		except ValueError:
			print("Not a numeric value, try again")



