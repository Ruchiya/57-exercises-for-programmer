from tkinter import filedialog
import os

name = []

def browse_file():
    """Open the data file"""
    browse= filedialog.askopenfilename(
        initialdir = os.getcwd(),
        title ='Select File',
        filetypes = [('text files','.txt')])
    return browse

def process_list(file):
    """Clean each file line and append to a list"""
    for i in file:
        clean = i.strip().split(',')
        name.append(clean)

browsing = browse_file()
r=open(browsing,'r')
process_list(r)

last= len(max(name)[0])+1 
first=len(max(name)[1])+1
salary= len(max(name)[2])+1

print('Last' + (' '* (last- len('last'))),
      'First' +(' '* (first- len('first'))),
      'Salary'+(' '* (salary- len('salary')))
      )
print('-' * (last+first +salary+1))
for i in sorted(name):
            print(
                i[0] + (' '* (last - len(i[0]))),
                i[1] + (' ' * (first - len(i[1]))),
                i[2] + (' ' * (salary - len(i[2]))),
                )

