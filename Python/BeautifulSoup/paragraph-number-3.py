# Write a Python program to get the number of paragraph tags of a given html document.
# Output: Number of paragraph tags: 33

import requests
from bs4 import BeautifulSoup

link = "https://www.linguanaturalis.com/"
request = requests.get(link)
html_document = BeautifulSoup(request.text, "html.parser")
all_paragraphs = html_document.find_all('p')

print(f"Number of paragraph tags: {len(all_paragraphs)}") 