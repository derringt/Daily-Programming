from sys import argv

max = int(argv[1])

sm = 1

for x in range(1,max+1):
    y = 2
    if sm % x == 0: continue
    while sm*y % x != 0: y += 1
    sm *= y

print sm
