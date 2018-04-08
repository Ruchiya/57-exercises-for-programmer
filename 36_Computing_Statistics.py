#Challenge included
import math

num_list = []

message = {}

def mean(num_list):
    mean = sum(num_list)/len(num_list)
    return mean
    
def minimum(num_list):
    minimum = min(num_list)
    return minimum

def maximum(num_list):
    maximum = max(num_list)
    return maximum

def std(num_list):
    average = mean(num_list)
    square_value = 0
    for num in num_list:
        y = (num-average)**2
        square_value += y
    std = round((square_value/ len(num_list))**0.5, 2)
        
    return round(std,2)
    
def main():
    while True:
        number = input('Enter a number, type \'done when finish\':').lower()
        if number == 'done':
            break
        else:
            num_list.append(int(number))
    print(f'Numbers:{num_list}')
    print(f'Average: {mean(num_list)}')
    print(f'Minimum: {minimum(num_list)}')
    print(f'Maximum: {maximum(num_list)}')
    print(f'Standard Deviation: {std(num_list)}')


if __name__ == '__main__':
    main()
        
