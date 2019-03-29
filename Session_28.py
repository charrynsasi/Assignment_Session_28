
import re
import nltk
import urllib.request
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")

text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))

c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
print (c.most_common()) # prints most common words staring at most common.