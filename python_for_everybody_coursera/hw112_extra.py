import re
nlist = []
numstrings = []
count = 0
fname = raw_input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    numstrings = re.findall('^New Revision.*:(\d+)',line)
    nlist.extend(numstrings)
    count = count+1
print nlist
average = 0
for i in nlist:
    i = int(i)
    total = total + i
    average = total/count
print average
