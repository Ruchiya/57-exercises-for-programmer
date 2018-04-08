def formula(rate):
    years = 72/rate
    return years

while True:
    try:
        rate = int(input('What is the rate of return: '))
        if rate == 0:
            print('Sorry, 0 is not a valid input')
            continue
        print( f'It will take {formula(rate):.0f} years to double your initial investment')
        break
    except ValueError:
        print('Sorry, Thats\' not a valid input')

        
