amount = round(float(input("What is the order amount?:")),2)
state = input("What is the state?:").lower()

if state == "wi" or state == "wisconsin":
	tax = amount * 0.055
	total = round(amount + tax,2)
	print(f"The subtotal is ${amount}\nThe tax is ${tax}\nThe total is ${total} ")
else:
	print(f"The total is {amount}")