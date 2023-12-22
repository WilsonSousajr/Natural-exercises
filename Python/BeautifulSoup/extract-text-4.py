# Write a Python program to extract the text in the first paragraph tag of a given html document.
# Output: All our teachers are university-educated, native speakers of the language they teach 
# and undergo rigorous training in the Natural methodology. Find out more about them:

import requests
from bs4 import BeautifulSoup

link = "https://www.linguanaturalis.com/"
request = requests.get(link)
html_document = BeautifulSoup(request.text, "html.parser")
text_in_the_first_paragraph = html_document.p.string

print(text_in_the_first_paragraph)