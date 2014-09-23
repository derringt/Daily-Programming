T = int(raw_input())

def recurse(n):
    if n % 3 == 0:
        for x in xrange(0,n):
            ans.append('5')
        return
    else:
        ans.append('33333')
        recurse(n-5)
        return

for i in range(0,T):
    ans = []
    n = int(raw_input())
    if str(n) in ['0','1','2','4','7'] or n < 0:
        print "-1"
    else:
       recurse(n)
    ans.reverse()
    print ''.join(ans)

