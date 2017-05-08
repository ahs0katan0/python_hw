
input = raw_input("Enter a score between 0.0 and 1.0:")

try:
    score = float(input)
except:
    print "Entry is incorrect. Retry entering a score between 0.0 and 1.0"
    exit()
if score > 1.0 or score < 0:
    print "Value needs to be equal or lower than 1.0 and more than 0.0"
else:
    if score >= 0.9:
        print "A"
    elif score >= 0.8:
        print "B"
    elif score >=0.7:
        print "C"
    elif score >= 0.6:
        print "D"
    else:
        print "F"
