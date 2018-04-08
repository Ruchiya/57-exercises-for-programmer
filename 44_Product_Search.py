import json
from tkinter import filedialog
import os

price = {}
quantity = {}
product = []


def browse_file():
    """Open the data file"""
    browse= filedialog.askopenfilename(
        initialdir = os.getcwd(),
        title ='Select File',
        filetypes = [('.json','.json')])
    return browse

path = browse_file()

with open(path, encoding = 'utf-8') as json_file:
    json_data = json.load(json_file)
    for item in range(len(json_data['products'])):
        product.append(json_data['products'][item])

for i in range(len(product)):
    price[product[i]['name']]=product[i]['price']
    quantity[product[i]['name']]=product[i]['quantity']

while True:
    try:
        search = input('What is the product name? >')
        print(f'Name: {search}\nPrice: ${price[search]}.00\nQuantity on hand:{quantity[search]}')
        break
    except:
        print('Sorry, that product was not found in our inventory')
