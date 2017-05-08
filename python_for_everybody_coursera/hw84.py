fhand = open('romeo.txt')
uniquelist = []
for line in fhand:
    line = line.rstrip()
    indivlines = line.split()
#    print indivlines
    for word in indivlines:
        if not word in uniquelist:
            uniquelist.append(word)
            sortedwords = uniquelist.sort()
print uniquelist