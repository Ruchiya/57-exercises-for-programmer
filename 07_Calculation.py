import math
conver = 0.09290304*100

while True:
    try:
        metric = input("Choose a metric, enter 'm' for meter and 'f' for feet:")
        if metric == 'f':
            length = int(input("What is the length of room in feet:"))
            width = int(input("What is width of room in feet:"))
            area_s = length* width
            area_m = (area_s*conver)/100
            print('You\'ve entered dimensions of {} feet by {} feet'.format(length, width))
            print('The area is\n{} square feet\n{} square meters'.format(round(area_s,3), round(area_m,3)))
        elif metric == 'm':
            length = int(input("What is the length of room in meters:"))
            width = int(input("What is width of room in meters:"))
            area_m = length *width
            area_s = area_m/conver
            print('You\'ve entered dimensions of {} meters by {} meters'.format(length, width))
            print('The area is\n{} square meters\n{} square feet'.format(round(area_m,3),round(area_s,3)))
        else:
            raise ValueError
        break
    except ValueError:
        print("Not the correct value, try again..")
