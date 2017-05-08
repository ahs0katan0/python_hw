fhand = open('mbox-short.txt')
#uniquelist = []
uniquenames = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        indivlines = line.split()
        name = indivlines[1]
        uniquenames[name] = uniquenames.get(name,0) + 1
        #uniquelist.append(names)
#        print "Names: ", uniquelist
#for name in uniquelist:
#    uniquenames[name] = uniquenames.get(name,0) + 1
print uniquenames

bigcount = None
bigword = None
for name,count in uniquenames.items():
    if bigcount is None or count > bigcount:
        bigword = name
        bigcount = count
print bigword, bigcount