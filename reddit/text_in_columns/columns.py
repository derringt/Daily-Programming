#Reddit Challenge 182, http://redd.it/2hssx6
#Takes text from input.txt, formats it into columns
f = open('input.txt')

#First line in format:
#<number of colums> <column maximum width> <spacees between maxwidth columns>
cols, colwidth, spacewidth = [int(x) for x in f.readline().rstrip().split(' ')]

build = ['']

#Start building column-width text
for line in f:
    words = line.split(' ')
    for w in words:
        #New row if the word is too long
        if len(build[-1]) + len(w.rstrip()) + 1 > colwidth:
                build.append('')
        #Add spaces between words
        if len(build[-1]) > 0:
            build[-1] += ' '
        build[-1] += w.rstrip()
        #When you hit a newline, make a new row
        if '\n' in w:
            build.append('')

#Calculate number of rows, making it as even as possible.
rows = (len(build) / cols) + (len(build) % cols)

final = []

#Pad out the columns so we don't overflow
for x in xrange(0,cols+1):
    build.append('')

for r in xrange(0,rows):
    final.append('')
    for c in xrange(0, cols):
        final[-1] += build[r + c*rows] 
        #Add spaces between columns
        final[-1] += ' ' * (colwidth - len(build[r+c*rows]) + spacewidth)

o = open('output.txt', 'w')
for l in final:
    o.write(l)
    o.write('\n')
