def calculation(first, second):
    p = first + second
    s = first - second
    m = first * second
    d = first / second
    print( '{} + {} = {}\n'.format(first, second, p),
           '{} - {} = {}\n'.format(first, second,s),
           '{} * {} = {}\n'.format(first, second,m),
           '{} / {} = {}\n'.format(first, second,d))

while True:
    try:
        first = int(input("What is the first number?:"))
        second = int(input("What is the second number?:"))
        calculation(first, second)
        break
    except ValueError:
        print("Try again")

