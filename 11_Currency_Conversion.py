amount = float(input("How many euro are you exchanging:"))
rate = float(input("What is the exchange rate:"))

amountto = round((amount*rate)/100, 2)

print(f"{amount} euros at an exchange rate of {rate} is {amountto} U.S. dollars")
