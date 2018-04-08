import random

special = '`-=[];\',./~!@$%^&*()_+{}|:"<>?'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
password = []


length = int(input('Minimum Length? > '))
sc = int(input('No. of special character? > '))
num = int(input('No. of numbers? > '))

for i in range(num):
        password.append(str(random.randint(0, 9)))
        
for i in range(sc):
    password.append(random.choice(special))


for i in range(length-(sc+num)+1):
    password.append(random.choice(alphabet))

        
random.shuffle(password)
shuffle = ''.join(password)

print(f'Your password is {shuffle}')

