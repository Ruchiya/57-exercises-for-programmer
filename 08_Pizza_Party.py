people = int(input('How many people?:'))
pizza = int(input('How many pizza do you have?:'))
pslice = int(input('Number of slice per pizza?:'))

totalSlice = pizza*pslice
slicePerPerson = totalSlice//people


if totalSlice % people ==0:
    if slicePerPerson == 1:
        print('{} people with {} pizzas\nEach person gets {} piece of pizza.\nThere are 0 leftover piece'.format(people, pizza,slicePerPerson, pslice))
    else:
        print('{} people with {} pizzas\nEach person gets {} pieces of pizza.\nThere are 0 leftover piece'.format(people, pizza,slicePerPerson, pslice))
else:
    if slicePerPerson == 1:
        if totalSlice % people ==1:
            print('{} people with {} pizzas\nEach person gets {} piece of pizza.\nThere are {} leftover piece'.format(people, pizza,slicePerPerson,totalSlice%people))
    else:
        print('{} people with {} pizzas\nEach person gets {} pieces of pizza.\nThere are {} leftover pieces'.format(people, pizza,slicePerPerson,totalSlice%people))
    

#Variant of the program

pizza = int(input('Choose a 4, 6, or 8 slice pizza(please enter number of slice per pizza): '))
people = int(input('How many people?:'))
slices = int(input('Number of pieces each person wants?:'))

totalSlice = people*slices
totalPizza = totalSlice//pizza

if totalSlice % pizza == 0:
    print('You will need {} full pizzas'.format(totalPizza))
else:
    print('You will need {} full pizzas'.format(totalPizza+1))
