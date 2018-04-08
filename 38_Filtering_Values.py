def filterEvenNumber(numlist):
    new = []
    for i in numlist:
        if int(i)%2 == 0:
            new.append(i)
    return 'The even numbers are ' + ' '.join(str(i) for i in new)

num = input('Enter a list of number, separated by spaces:').split()

    
print(filterEvenNumber(num))
        
