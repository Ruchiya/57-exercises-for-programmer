import math

gallon = 350

class room(object):
    
    def __init__(self, length, width,):
        self.length = length
        self.width = width

    def rectangle_room(self):
        area = self.length * self.width
        
        pass
    
    def round_room(self,radius):
        self.radius = radius
        area = self.radius**2 * 3.14
        paint= int(area//gallon)
        return area,paint

    


while True:
    try:
        rtype = input("Select a room type\nEnter 'c' for round room\nEnter 'r' or 's' for rectangle/square room\nEnter 'l' for L-shaped room:")
        
        if rtype == ('r' or 's'):
            length = float(input("Length in meters:"))
            width = float(input("Width in meters:"))
            area = length * width
            paint = int(area//gallon)
            if area%gallon !=0:
                print('You will need to purchase {} gallons of paint to cover {} square meters'.format(paint+1, area))
            else:
                print('You will need to purchase {} gallons of paint to cover {} square meters'.format(paint, area))
        elif rtype == 'c':
            radius = float(input("Radius in meters:"))
            area = radius**2 * 3.14159
            paint = int(area//gallon)
            if area%gallon !=0:
                print('You will need to purchase {} gallons of paint to cover {} square meters'.format(paint+1, area))
            else:
                print('You will need to purchase {} gallons of paint to cover {} square meters'.format(paint, area))
        elif rtype == 'l':
            firLength= float(input('Please break up your room into two rectangles\nEnter length of first rectangle:'))
            firWidth= float(input('Enter width of first rectangle:'))
            secLength= float(input('Enter length of second rectangle:'))
            secWidth= float(input('Enter width of second rectangle:'))
            area = firLength*firWidth + secLength*secWidth
            paint = int(area//gallon)
            if area%gallon !=0:
                print('You will need to purchase {} gallons of paint to cover {} square meters'.format(paint+1, area))
            else:
                print('You will need to purchase {} gallons of paint to cover {} square meters'.format(paint, area))
            
        break
    except ValueError:
        print("This is not a numeric value, try again")
