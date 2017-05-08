fname = raw_input("Enter file name: ")
count = 0
try:
    fhand = open(fname)
    for line in fhand:
        count = count + 1
    print "There were", count, "lines in ", fname
except: 
    if fname == "na na boo boo": 
        print "What a silly name for a file!"
    exit()

