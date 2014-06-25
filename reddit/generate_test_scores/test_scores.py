# First names and last names from:
# http://www.quietaffiliate.com/free-first-name-and-last-name-databases-csv-and-sql

import csv, sys, random

firstreader = csv.reader(open('first_names.csv', 'rU'))
lastreader = csv.reader(open('last_names.csv', 'rU'))

firstrows = list(firstreader)
totalfirst = len(firstrows)

lastrows = list(lastreader)
totallast = len(lastrows)

testscores = dict()

while len(testscores) < int(sys.argv[1]):
    first = str(firstrows[random.randint(0,totalfirst-1)])[2:-2]
    last = str(lastrows[random.randint(0,totallast-1)])[2:-2]

    lastfirst = last + ' , ' + first
    
    if not lastfirst in testscores:
        rand1 = random.randint(0,100)
        rand2 = random.randint(0,100)
        rand3 = random.randint(0,100)
        rand4 = random.randint(0,100)
        rand5 = random.randint(0,100)
        testscores[lastfirst] = ' '.join([`rand1`, `rand2`, `rand3`, `rand4`, `rand5`])
    else:
        print lastfirst + ' is a duplicate!!!'

data = open("test_data.txt", 'w')
for lastfirst in testscores:
    data.write(lastfirst + ' ' + testscores[lastfirst] + '\n')
data.close()
