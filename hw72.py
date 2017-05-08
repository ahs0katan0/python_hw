# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fhand = open(fname)
count = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
# print 'There were', count, 'lines in', fname
# print "Done"
total = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    if line.startswith("X-DSPAM-Confidence:"):
        line = line.rstrip()
        numberpos = line.find(":")
        actualnumb = line[numberpos+1:]
        actualnumb = float(actualnumb)
        total = total + actualnumb
        average = total/count
print 'Average spam confidence:',average