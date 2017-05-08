import sqlite3

conn = sqlite3.connect('hw2db.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'mbox.txt'
fhand = open(fname)

for line in fhand:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    domainpos = email.find("@")
    actualdomain = email[domainpos+1:]
#    print actualdomain
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (actualdomain, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES (?, 1 )''', (actualdomain, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (actualdomain, ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
