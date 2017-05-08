import urllib
import json

sum = 0
countlist = []

data = urllib.urlopen("http://python-data.dr-chuck.net/comments_311726.json").read()
hwdata = json.loads(data)
print (hwdata)

countlist = hwdata["comments"]

print 'Countslist:', countlist
for item in countlist:
    print 'Count', item['count']
    sum = sum + item['count']
print sum