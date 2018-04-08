import re

level = {1:'very weak',
        2:'weak',
        3:'okay',
        4:'strong',
        5:'very strong'}

def passwordValidator(password):
    special = "~`!@#$%^&*()_+-={}|:\"<>?[]\;',./"

    if len(password)<8:
        if password.isdigit() == True:
            return 1
        elif password.isalpha() == True:
            return 2

    elif len(password)>= 8:
        digit = re.search('\d+',password)
        alphabet = re.search('[a-zA-Z]',password)
        
        if bool(digit)== True and bool(alphabet)==True:
            for i in password:
                if i in special:
                    return 5
        return 4

    else:
        return 3
        
        
password = input('Password check:')
print(f'The password "{password}" is a {level[passwordValidator(password)]} password')

