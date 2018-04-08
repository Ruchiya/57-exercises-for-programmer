#Challenges included

import math

def credit(b,i,p):
    num = math.log10(1+(b/p)*(1-(1+i)**30))
    den = math.log10(1+i)
    n = math.ceil((-1/30) *(num/den))
    return n

def paypermonth(b,i,n):
    num = b*(1-(1+i)**30)
    den = (10**((-30)*(math.log10(1+i))*(n))-1)
    n = round(num/den,2)
    return n

while True:
    try:
        creditcheck = input('Would you like to check \'p\' to find out how long you need to pay for credit card, or \'m\' for montly payment:').lower()
        if creditcheck == 'p':
            b= float(input('What is your balance:'))
            i = float(input('What is the APR on the card(as a percent):'))/100/365
            p = float(input('What is the monthly payment you can make:'))
            print(f'It will take you {credit(b,i,p)} months to pay off this card.')
        elif creditcheck == 'm':
            b= float(input('What is your balance:'))
            i = float(input('What is the APR on the card(as a percent):'))/100/365
            n = int(input('How many months would you like to pay it out:'))
            print(f'You will need to pay ${paypermonth(b,i,n)} per month')
        else:
            raise ValueError
    except ValueError:
        ('Try again')







