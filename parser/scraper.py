
# coding: utf-8

import flask
import jinja2

app = flask.Flask(__name__)  # a Flask object

import urllib
from bs4 import BeautifulSoup

nyt_url = 'https://www.nytimes.com/2017/10/29/business/virtual-reality-driverless-cars.html'

def scrape_times_article(url):
    """Function that returns title, author, text and saves pertaining images
    from the article given URL address"""
    
    request_handle = urllib.request.urlopen(url)
    text = request_handle.read()
    text= text.encode('utf-8') # not always necessary
    soup = BeautifulSoup(text, 'html.parser')
    
    
    author = soup.find("meta", {'name':'byl'}).get('content')[3:]
    
    title = soup.title.text
    
    paragraphs = soup.find_all('p', class_="css-1cy1v93 e2kc3sl0") 
    # The structure of HTML of New York Times changes sometimes, so beware it. 
    
    url = soup.find("meta", {'name':'image'}).get('content')
    urllib.request.urlretrieve(url, "NYT.jpg")
    
    return title, author, paragraphs

@app.route('/')
def article():
    title, author, paragraphs = scrape_times_article(nyt_url)
    return flask.render_template('story_template.html', title = title, author = author, paragraphs = paragraphs)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 

