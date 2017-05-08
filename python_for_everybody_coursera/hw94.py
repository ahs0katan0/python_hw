fhand = open('mbox-short.txt')
uniquelist = []
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        indivlines = line.split()
        names = indivlines[1]
        uniquelist.append(names)
#        print "Names: ", uniquelist
uniquenames = dict()
for name in uniquelist:
    uniquenames[name] = uniquenames.get(name,0) + 1
#print uniquenames

bigcount = None
bigword = None
for name,count in uniquenames.items():
    if bigcount is None or count > bigcount:
        bigword = name
        bigcount = count
print bigword, bigcount