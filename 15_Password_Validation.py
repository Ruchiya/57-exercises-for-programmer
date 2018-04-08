user = {'user1':'password1'}

while True:
    log = input('Would you like to create log in? \'yes\' or \'no\':')
    if log == 'yes':
        username = input('Create your username:').strip()
        password = input("Create your password:").strip()
        register(username, password)
    elif log == 'no':
        break
    
while True:
    try:
        username = input('What is your username:').strip()
        password = input("What is the password:").strip()
        check = user[username]
        if check == password:
            print(f'Welcome {username} !')
        else:
            print(f'I don\'t know you')
            continue
    except KeyError:
        print('You didn\'t register...')
