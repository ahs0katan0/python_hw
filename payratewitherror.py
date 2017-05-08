r=10
h = raw_input()

try:
    h= int(h)
except:
    print "entry incorrect"
    exit()
if h > 40:
    overtimeh = h - 40
    pay = (overtimeh*1.5*r)+(40*r)
else:
    pay = h*r
print pay

