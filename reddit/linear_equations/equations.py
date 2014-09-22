import sys, re

def solve(a1=0, b1=0, a2=0, b2=0):
    if '.' in a1+b1+a2+b2:
        a1 = float(a1)
        b1 = float(b1)
        a2 = float(a2)
        b2 = float(b2)
    else:
        a1 = int(a1)
        a2 = int(a2)
        b1 = int(b1)
        b2 = int(b2)

    y = ((b2*a1)-(a2*b1))/(a1-a2)
    x = (y-b1)/a1
    if type(x) is float or type(y) is float:
        x = round(x, 4)
        y = round(y, 4)
    return [x,y]

eqs=[]
p = re.compile('y=\+?(-?\d*\.?\d+)x\+?(-?\d*\.?\d+)?')

for x in xrange(2):
    eq = raw_input("Enter equation " + str(x+1) + ": ")
    eqm = p.match(eq)
    eqs.append([eqm.group(1) or '0', eqm.group(2) or '0'])

x,y = solve(eqs[0][0], eqs[0][1], eqs[1][0], eqs[1][1])
print "(%s, %s)" % (x, y)
