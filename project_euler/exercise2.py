fib1 = 0
fib2 = 1
swap = 0
sum = 0

while fib2 < 4000000:
    if fib2 % 2 == 0:
        sum += fib2
    swap = fib2
    fib2 += fib1
    fib1 = swap

print sum
