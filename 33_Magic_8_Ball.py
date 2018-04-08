import random

ans = ['Yes', 'No', 'Maybe', 'Ask again later']
quest = input('What\'s your question?:')
print(f'{ans[random.randint(0,5)]}')
