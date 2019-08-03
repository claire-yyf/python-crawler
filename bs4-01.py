# get html

from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://www.facebook.com")
bsObject = BeautifulSoup(html, 'html.parser')

for link in bsObject.find_all('a'):  # find tag name
    # get text between tags, get href attribute
    print(link.text, link.get('href'))
