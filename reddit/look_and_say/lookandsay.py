#Look and Say Sequence
#Run script, enter <seed> <Nth term>
numbers, nth = raw_input().split()
print numbers

for x in xrange(1,int(nth)):
    new = []
    curr = ''
    for n in list(numbers):
        if not n == curr:
            new.append(1)
            new.append(n)
            curr = n
        else:
            new[-2] += 1
    numbers = ''.join([str(n) for n in new])
    print numbers
