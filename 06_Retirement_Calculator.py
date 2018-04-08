import datetime

now= datetime.datetime.now()
year = now.year

current = int(input("What is your current age?:"))
retire = int(input("What age would you like to retire?:"))
yrleft = retire - current
retireyr = year + yrleft

if yrleft <=0:
    print('Already Retire')
else:
    print('You have {} years left untill you can retire\nIt\'s {}, so you can retire in {}'.format(yrleft,year,retireyr))
