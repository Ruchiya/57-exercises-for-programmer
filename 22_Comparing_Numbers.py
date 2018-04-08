numList = []
check = 0

while True:
    number = input('Enter the number, Enter \'done\' if you no longer want to enter any number:')
    if number == 'done':
        break
    else:
        numList.append(number)

if len(numList) == 0 :
    print('There is no number to compare with')

elif len(numList)==1:
    print(f'The largest number is {numList[0]}')
    
else:
    for i in numList:
        i = int(i)
        if i>check:
            check = i 

print(f'The largest number is {check}')
        


