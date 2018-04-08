english = {'1':'January',
         '2':'Feburary',
         '3':'March',
         '4':'April',
         '5':'May',
         '6':'June',
         '7':'July',
         '8':'August',
         '9':'September',
         '10':'October',
         '11':'November',
         '12':'December'
         }

chinese = {'1':'一月',
           '2':'二月',
           '3':'三月',
           '4':'四月',
           '5':'五月',
           '6':'六月',
           '7':'七月',
           '8':'八月',
           '9':'九月',
           '10':'十月',
           '11':'十一月',
           '12':'十二月'
           }

language = input('Please choose a language to display the month\nType \'E\' for English, \'C\' for Chinese:').lower()

dictionary = str(input('Please enter the number of the month:')).strip()

if language == 'e':
    lookup = english[dictionary]
elif language == 'c':
    lookup = chinese[dictionary]

print(f'The name of the month is {lookup}.')
