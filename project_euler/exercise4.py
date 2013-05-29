isPalindrome = lambda num: str(num) == str(num)[::-1]

largest = 0
n = 0
m = 0
product = 0

while n < 999:
    while m < 999:
        product = (999 - n) * (999 - m)
        if isPalindrome(product) and product > largest: largest = product
        elif product < largest: break
        m += 1
    n += 1
    m = 0

print largest
        
