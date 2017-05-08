import string
fhand = open('longestpoemtextwiki.txt')
alphablist = list()
uniqueletters = dict()
for line in fhand:
    line = line.lower()
    for char in line:
        if char.isalpha():
            uniqueletters[char] = uniqueletters.get(char,0) + 1
print uniqueletters
for alphab,count in uniqueletters.items():
    alphablist.append((count,alphab))
alphablist.sort(reverse=True)
for count,alphab in alphablist:
    print alphab, count