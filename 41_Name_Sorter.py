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
    for i in file:
        clean = i.strip().split(',')
        name.append(clean)

f = browse_file()
r = open(f,'r')
process_list(r) 

print('Total of 7 names\n-----------------')
for i in sorted(name):
    print(i[0],',',i[1])
