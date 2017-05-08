# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
contentslist = []
clist = []
total = 0
soup = BeautifulSoup(html)
# Retrieve all of the span tags
tags = soup('span')


for tag in tags:
    # Look at the parts of a tag
    print 'TAG:',tag
    print 'Contents:',tag.contents[0]
    print 'Attrs:',tag.attrs
    contentslist = re.findall('[0-9]+',tag.contents[0])
    clist.extend(contentslist)
print clist
for i in clist:
    i = int(i)
    total = total + i
print total
