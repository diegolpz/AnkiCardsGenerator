#!/usr/bin/env python3

import re
from bs4 import BeautifulSoup

with open("test.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

textOfTableIWant = soup.find(string=re.compile("([Ii]nfinitive|[Nn]ominative)"))
tableIWant = textOfTableIWant.find_parent("table")
# The next block disables the hyper links to the wiktionary page of the words in de table
for child in tableIWant.find_all(True):
    if child.has_attr('href'):
        del child['href']
print( tableIWant )
