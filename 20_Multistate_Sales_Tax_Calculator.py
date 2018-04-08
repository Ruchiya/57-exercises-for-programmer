order = float(input("Please enter order amount:"))
state = input("What state do you live in ").lower()

if state == 'wisconsin':
	county = input("What county do you live in ")

	if county == 'eau claire':
		tax = 0.05*order
		total = round(order+tax,2)
		print(f'The tax is ${tax}\nThe total is ${total}')

	elif county == 'dunn':
		tax = 0.04*order
		total = round(order+tax ,2)
		print(f'The tax is ${tax}\nThe total is ${total}')

	else:
		print(f'The total is ${order}')

elif state == 'illinois':
	tax = 0.08*order
	total = round(order+tax,2)
	print(f'The tax is ${tax}\nThe total is ${total}')

else:
	print(f'The total is ${order}')