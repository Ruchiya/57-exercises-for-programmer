import math
subtotal = 0
counter = 1

while True:
    try:
        price = float(input(f'Enter the price of item {counter}:'))
        quantity = int(input(f'Enter the quantity of item {counter}:'))
        subtotal += price*quantity
        counter+=1
        finish = (input('Is there more item? Enter \'yes\' or \'no\':'))
        if finish == 'yes' or finish == 'y':
            continue
        elif finish == 'no' or finish == 'n':
            break
    except ValueError:
        print('Not Numeric, try again')

tax = math.ceil((subtotal*100 * 0.055))/100
total = tax +subtotal

print(f'Subtotal:${subtotal}\nTax:${tax}\nTotal:${total}')
