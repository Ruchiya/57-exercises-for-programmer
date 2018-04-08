
#Used New York Times Movie API

"""
Rotten Tomato API is no longer available

Using the Movie Reviews API from New York Times
"""

import json
import urllib.request

def movie_search(movie):
    """validate the movie and return json data"""
    api = ''
    with open('50_api.txt','r') as f: #Save API Key to a text file
        read_data = f.read()
        api += read_data
    f.close()
    api += read_data
    url = f'http://api.nytimes.com/svc/movies/v2/reviews/search.json?query={movie}&api-key={api}'
    response = urllib.request.urlopen(url)
    with response as api:
        data = json.loads(api.read().decode())
        
    return data

movie = movie_search(input('Enter the name of a movie >').replace(' ','%20'))

#If the result == 1
try:
    title = movie['results'][-1]['display_title']
    rating=movie['results'][-1]['mpaa_rating']
    summary=movie['results'][-1]['summary_short']
    print(f"""Title: {title}
Rating: {rating}
Summary: {summary}""")
except IndexError:
    print('Movie name error')
