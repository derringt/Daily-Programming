sumsquares = 0
squaredsum = 0

for x in range(1,101):
  sumsquares += x*x
  squaredsum += x

squaredsum *= squaredsum

print squaredsum - sumsquares
