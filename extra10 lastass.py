fhand = open('longestpoemtextwiki.txt')
wordslist = []
lettersdict = []
for line in fhand:
    line = line.translate(None, string.punctuation)
    line = line.lower()
    wordslist = line.split()
print wordslist
    
