def max_power(n):
    for i in xrange(2,n):
        x = n
        y = 0
        if i*i > n: break
        while x % i == 0:
            x /= i
            y += 1
            if x == 1: return y
    return 1
