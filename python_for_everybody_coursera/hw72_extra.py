#did hw72 extra in Chap 7 using lists from Chap 8
fhand = open('mbox-short.txt')
count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"): continue
    line = line.split()
    number = line[1]
    number = float(number)
    total = total + number 
    count = count +1
    average = total/count
print total
print "Average spam confidence:", average