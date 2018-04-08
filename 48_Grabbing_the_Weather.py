#http://api.openweathermap.org/data/2.5/weather?q={country}&appid={API Key :xxxxxxxx}

import json
import urllib.request

weather_api = ''

with open('48_api.txt','r') as f: #Save API Key to a text file
    read_data = f.read()
    weather_api += read_data
f.closed

def url_append(country):
    '''Append the input country with url '''
    url=f'http://api.openweathermap.org/data/2.5/weather?q={country[0]}&appid='+weather_api
    return url

def api_response(country):
    '''Open the API and return response'''
    try:
        response = urllib.request.urlopen(url_append(country))
        return response
    except:
        return None
    
def json_python(api):
    data = json.loads(api.read().decode())
    temp = data['main']['temp']
    return temp

def kelvin_fahrenheit(kelvin):
    '''Convert kelvin to fahrenheit'''
    f = 1.8 * (kelvin-273)+ 32
    return round(f)

country = input('where are you? >').split()

json_data = api_response(country)

try:
    with json_data as api:
        data= json_python(api)
        fahrenheit = kelvin_fahrenheit(data)
        print(f'{country[0]} weather:\n{fahrenheit} degrees Fahrenheit')
except AttributeError:
    print ('Invalid country')
