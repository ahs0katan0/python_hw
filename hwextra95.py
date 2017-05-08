fhand = open('mbox-short.txt')
#domainlist = []
uniquedomdict = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith("From: "):
        indivline = line.split()
        domainelement = indivline[1]
#        domainlist.append(domainelement)
#print domainlist
        domainpos = domainelement.find("@")
        actualdomain = domainelement[domainpos+1:]
        uniquedomdict[actualdomain] = uniquedomdict.get(actualdomain,0) + 1
print "Domains: ", uniquedomdict

