fhand = open('mbox-short.txt')
weekdaycount = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        indivlines = line.split()
        weekday = indivlines[2]
        weekdaycount[weekday] = weekdaycount.get(weekday,0) + 1
#        print "Days: ", weekdaycount
print weekdaycount

