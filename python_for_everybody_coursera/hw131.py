import urllib
import xml.etree.ElementTree as ET

input ='http://python-data.dr-chuck.net/comments_311722.xml'
url = urllib.urlopen(input).read()

sum = 0
tree = ET.fromstring(url)

lst = tree.findall('comments/comment/count')
print lst
for item in lst:
    item = float(item.text)
    print item
    sum = sum + item
print sum
