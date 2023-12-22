# Write a Python program to extract all the URLs from the webpage python.org 
# that are nested within <li> tags from .
# Output: ['#', '/en/natural/method/', '#', '#', '/en/natural/contact/', '#', 
# '/en/natural/courses/english/#teachers', '/en/natural/courses/english/']

import requests
from bs4 import BeautifulSoup

link = "https://www.linguanaturalis.com/"
request = requests.get(link)
urls = []
html_document = BeautifulSoup(request.text, "html.parser")

for links in html_document.find_all('li'):
    a = links.find('a')
    try:
        if 'href' in a.attrs:
            urls.append(a.attrs['href'])
    except:
        pass
    
print(urls)


