# Write a Python program to retrieve all the paragraph tags from a given html document.

import requests
from bs4 import BeautifulSoup

link = "https://www.linguanaturalis.com/"
request = requests.get(link)
html_document = BeautifulSoup(request.text, "html.parser")
all_paragraphs = html_document.find_all('p')

print(all_paragraphs) 