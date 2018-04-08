def heartrate(pulse,age, intensity):
    rate = (((220-age)-pulse)*intensity/100)+pulse
    return rate

while True:
    try:
        pulse = int(input('Resting Pulse:'))
        age = int(input('Age:'))
        break
    except ValueError:
        print('Invalid, try again')


print('Intensity','\tRate' )
for i in range(55, 100, 5):
    print(f'{i}%', f'\t\t{heartrate(pulse,age,i):.0f} bmp')
