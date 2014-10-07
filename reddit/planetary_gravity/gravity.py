from math import pi

G = 6.67e-11
mass = float(raw_input())
T = int(raw_input())

print
for x in xrange(0,T):
    planet, rad, d = raw_input().split(',')
    rad, d = float(rad), float(d)
    pvol = 4./3. * pi * rad**3
    pmass = pvol * d
    force = G * (pmass * mass)/(rad**2)
    print '%s: %.3f' % (planet, force)
