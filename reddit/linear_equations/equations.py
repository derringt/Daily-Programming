import sys, re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#Solve 2-variable linear equations in the form y = ax + b
def solve(a1=0, b1=0, a2=0, b2=0):
    y = ((b2*a1)-(a2*b1))/(a1-a2)
    x = (y-b1)/a1
    if x.is_integer():
        x=int(x)
    if y.is_integer():
        y=int(y)
    if type(x) is float or type(y) is float:
        #Round to ten-thousandths place per spec
        x = round(x, 4)
        y = round(y, 4)
    return [x,y]

def graph(a1, b1, a2, b2, x, y):
    x1 = np.array(range(-10,11))
    y1 = formula(a1, b1, x1)
    x2 = np.array(range(-10,11))
    y2 = formula(a2, b2, x2)
    plt.plot(x1, y1, 'b-', x2, y2, 'r-', x, y, 'ko')
    plt.axvline(ymin=-10,ymax=10,ls='--',color='k')
    plt.axhline(xmin=-10,xmax=10,ls='--',color='k')
    plt.annotate('('+str(x)+','+str(y)+')',xy=(x,y), xycoords='data', xytext=(x+5,y-5), textcoords='offset points')
    plt.savefig('test.png',format='png')

def formula(a, b, x):
    return a * x + b

eqs=[]
#Assuming input is in format y = ax + b, with a required and b optional
p = re.compile('y=\+?(-?\d*\.?\d+)x\+?(-?\d*\.?\d+)?')

for x in xrange(2):
    eq = raw_input("Enter equation " + str(x+1) + ": ")
    eqm = p.match(eq)
    eqs.append([float(eqm.group(1) or '0'), float(eqm.group(2) or '0')])

x,y = solve(eqs[0][0], eqs[0][1], eqs[1][0], eqs[1][1])
graph(eqs[0][0], eqs[0][1], eqs[1][0], eqs[1][1], x, y)
print "(%s, %s)" % (x, y)
