import math

def max_power(n):

    for i in xrange(2,int(round(math.sqrt(n)))+2):
        x = 2
        while True:
            if math.pow(i,x) == n: return x
            if math.pow(i,x) > n : break
            x += 1
    return 1
