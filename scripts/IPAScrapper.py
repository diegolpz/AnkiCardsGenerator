#!/usr/bin/env python3

import re
from bs4 import BeautifulSoup

with open("test1.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

textOfTableIWant = soup.find("span","IPA")
print(textOfTableIWant.string)
