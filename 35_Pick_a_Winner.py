import random

winner = []

while True:
    name = input('Enter a name:')
    if name == ' ':
        break
    else:
        winner.append(name)


win = random.randint(0, len(winner))
print(f'The winner is ...{winner[win]}!')
