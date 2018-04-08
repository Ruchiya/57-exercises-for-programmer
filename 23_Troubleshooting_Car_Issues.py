Q1 = input('Is the car silent when you turn the key? y or n:')

if Q1 == 'y':
    Q2 = input('Are the battery terminals corroded? y or n:')
    if Q2 == 'y':
        print('Clean terminals and try starting again.')
    else:
        print('Replace cables and try again.')
else:
    Q2 = input('Does the car make a clicking noise?? y or n:')
    if Q2== 'y':
        print('Replace the battery.')
    else:
        Q3 = input('Does the car crank up but fail to start?? y or n:')
        if Q3 == 'y':
            print('Check spark plug connections.')
        else:
            Q4 = input('Does the engine start and then die?? y or n:')
            if Q4 =='y':
                Q5 = input('Does your car have fuel injection? y or n:')
                if Q5 == 'y':
                    print('Get it in for service')
                else:
                    print('Check to ensure the choke is opening and closing')
            else:
                print('Go to car service to check')
                    

