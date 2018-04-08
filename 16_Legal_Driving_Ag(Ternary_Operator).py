age = int(input('What is your age:'))

#Ternary Operator
print('You are not old enough to drive legally') if age < 16 else print('You are legal to drive')

legal_driving = {'US':16,
                 'Canada':16
                 'Fiji':17
                 'China':18
    }

while True:
    try:
        age = int(input('What is your age:'))
        break
    except ValueError:
        print('Enter a valid age')
        
