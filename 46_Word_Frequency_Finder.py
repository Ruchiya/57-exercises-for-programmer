from collections import Counter

with open('46_data.txt', 'r') as file:
    data =file.read().split()
    frequency = Counter()
    for word in data:
        frequency[word]+=1

    for key, value in sorted(frequency.items()):
        print(key,':',value*'*')
