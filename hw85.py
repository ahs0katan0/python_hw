fhand = open('mbox-short.txt')
names = []
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "): continue
    line = line.split()
    name = line[1]
    count = count +1
    print name
print "There were", count, "lines in the file with From as the first word"