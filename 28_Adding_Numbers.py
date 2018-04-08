total = 0
occurence = int(input('How many number?:'))

for i in range(occurence):
    try:
        num = float(input('Enter a number:'))
        total += num
    except ValueError:
        pass
    
print(f'The total is {total:.0f}')
