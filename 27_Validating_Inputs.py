def validateInput(firstName, lastName,ID,zipcode):
    c1 = validateName(firstName)
    c2 = validateName(lastName)
    c3 = validateID(ID)
    c4 = validateZipcode(zipcode)
    if (c1 and c2 and c3 and c4) == 'True':
        print('There were no errors')
    else:
        for boolean in c1,c2,c3,c4:
            if boolean == True:
                continue
            else:
                print(boolean)
                
def validateName(name):
    if len(name) >=2:
        if name.isalpha() == True:
            return True
        else:
            return f'{name} is not a valid name'
    else:
        return f'{name} is not a valid name. It is too short'

    
def validateID(ID):
    if len(ID)!=7:
        return 'This is not a valid ID'
    else:
        char = ID[:3]
        hy = ID[3]
        num = ID[3:]
        if char.isalpha() == False:
            return 'This is not a valid ID'
        if hy !='-':
            return 'This is not a valid ID'
        if num.isdigit() == False:
            return 'This is not a valid ID'
        return True
    
def validateZipcode(zipcode):
    if zipcode.isdigit() == True: 
        return True
    else:
        return 'The ZIP code must be numeric'

firstname = input('Enter the first name:').strip()
lastname = input('Enter the lastname:').strip()
zipcode = input('Enter the zipcode:').strip()
ID = input('Employee ID:').strip()

validateInput(firstname,lastname,ID, zipcode)
