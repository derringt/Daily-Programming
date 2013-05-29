largest = 0
for n in range(999,100,-1):
    if n * 999 < largest: break
    for m in range(999,100,-1):
        if n*m < largest: break
        elif str(n*m) == str(n*m)[::-1]: largest = n*m

print largest
