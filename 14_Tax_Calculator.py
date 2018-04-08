while True:
    amount = float(input('What is the order amount:'))
    state = input("What is the state:").lower()
    if state == 'wi' or state == 'wisconsin':
        tax = amount*0.055
        total = round(tax + amount,2)
        print(f'The subtotal is ${amount}')
        print(f'The tax is ${tax}')
        print(f'The total is {total}')
        break
    print(f'The total is ${amount}')
    break
    

