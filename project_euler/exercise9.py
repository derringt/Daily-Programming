for a in range(1,1000):
    for b in range(a+1,1000):
        c = 1000 - a - b
        if a > c or b > c:
            break
	if a*a + b*b == c*c:
            print a*b*c
            break
