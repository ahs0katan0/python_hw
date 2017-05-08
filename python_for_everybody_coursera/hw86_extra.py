largest = None
smallest = None
numberslist = []
while True:
    num = raw_input("Enter a number and when you are done type in done: ")
    if num == "done" : 
        break
    try:
        int_num = int(num)
        numberslist.append(int_num)
    except:
        print "Invalid input"
# print numberslist 
min = min(numberslist)
min = float(min)
max = max(numberslist)
max = float(max)
print "Minimum: ", min
print "Maximum: ", max



 
#THIS WAS THE OLD CHAP 5 homework
#        if smallest is None:
#        smallest = int_num
#    elif int_num < smallest:
#        smallest = int_num
        
#    if largest is None:
#        largest = int_num
#    elif int_num > largest:
#        largest = int_num
    
#print "Maximum is", largest
#print "Minimum is", smallest

