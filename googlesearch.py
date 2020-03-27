#!usr/bin/python3

import sys, webbrowser
from googlesearch import search

print("Following top search results from google")
for urlopen in search(query=' '.join(sys.argv[1:]),num=5,stop=5):
     print(urlopen)
     webbrowser.open(urlopen)
