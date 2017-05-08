i=0
j=0
mylist = list()
for i in xrange(100):
    for j in xrange(100):
        for k in xrange(100):
            mylist.append(k + j *100 + i * 10000)
#            mylist.sort()
mylist.sort()            
print "done"          