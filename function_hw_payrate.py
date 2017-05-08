### Start of function
def computepay(hr, rt):
    if hr > 40:
        overtimeh = hr - 40
        totalpay = (overtimeh*1.5*rt)+(40*rt)
    else:
        totalpay = hr*rt
    return totalpay
### End of function
        
h = raw_input("Enter Hours:")
try:
    hours = float(h)
except:
    print "entry incorrect"
    exit()
    
r = raw_input("Enter Rate per hour:")
try:
    rate = float(r)
except:
    print "entry incorrect"
    exit()

p = computepay(hours, rate)
print p