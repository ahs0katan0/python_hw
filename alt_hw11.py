import re
nlist = []
numstrings = []
fhand = open('regex_sum_311720.txt')
for line in fhand:
    line = line.rstrip()
    numstrings = re.findall('[0-9]+',line)
    nlist.extend(numstrings)
print nlist
total = 0
for i in nlist:
    i = int(i)
    total = total + i
print total
