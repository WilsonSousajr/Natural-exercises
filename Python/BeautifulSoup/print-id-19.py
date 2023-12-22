# Write a Python program to print the element(s) that has a specified id of a given web page.

import requests
from bs4 import BeautifulSoup

link = "https://www.linguanaturalis.com/"
request = requests.get(link)
html_document = BeautifulSoup(request.text, "html.parser")
element_id = '#main_navbar'

print(html_document.select_one(element_id))