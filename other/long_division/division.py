num = float(raw_input("Enter the numerator:"))
denom = float(raw_input("Enter the denominator:"))
prec = int(raw_input("Enter the number of decimal places to calculate:"))

whole = int(num/denom)
result = []
new = (num % denom) * 10
while len(result) < prec:
    if new > denom or new == 0:
        result.append(int(new/denom))
        new = (new % denom) * 10
    else:
        new *= 10
        result.append(0)

print "%g.%s" % (whole, ''.join([str(i) for i in result]))
