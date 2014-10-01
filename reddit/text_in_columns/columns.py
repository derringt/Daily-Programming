f = open('input.txt')

cols, colwidth, spacewidth = [int(x) for x in f.readline().rstrip().split(' ')]
build = ['']

for line in f:
    words = line.split(' ')
    for w in words:
        if len(build[-1]) + len(w.rstrip()) + 1 > colwidth:
                build.append('')
        if len(build[-1]) > 0:
            build[-1] += ' '
        build[-1] += w.rstrip()
        if '\n' in w:
            build.append('')

rows = (len(build) / cols) + (len(build) % cols)
final = []

for x in xrange(0,cols+1):
    build.append('')

for r in xrange(0,rows):
    final.append('')
    for c in xrange(0, cols):
        final[-1] += build[r + c*rows] 
        final[-1] += ' ' * (colwidth - len(build[r+c*rows]) + spacewidth)

o = open('output.txt', 'w')
for l in final:
    o.write(l)
    o.write('\n')
