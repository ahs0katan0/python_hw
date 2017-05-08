fhand = open('mbox-short.txt')
actualhrlist=[]
hrdict = dict()
hrlist = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        indivline = line.split()
        timeelement = indivline[5]
        #print timeelement
        #hrpos = timeelement.find(":")
        actualhr = timeelement[:2]
        actualhrlist.append(actualhr)
#        print actualhrlist
for hrelement in actualhrlist:
    hrdict[hrelement]=hrdict.get(hrelement,0)+1
#print hrdict
for hr,count in hrdict.items():
    hrlist.append((hr,count))
#print hrlist
    hrlist.sort()
for hr,freq in hrlist:
    print hr, freq