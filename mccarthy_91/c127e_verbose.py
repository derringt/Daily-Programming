import sys
from sys import argv

number = int(argv[1])
recursions = 1
reason = "\n"

def mccarthy_verbose(n):

	global recursions
	global reason
	if recursions > 0:
		for i in xrange(recursions):
			sys.stdout.write('M(')
		sys.stdout.write(str(n))
		for i in xrange(recursions):
			sys.stdout.write(')')
		sys.stdout.write(reason)

	if n > 100:
		recursions = recursions - 1
		reason = ' since {0!s} is greater than 100\n'.format(n)
		if recursions == 0:
			sys.stdout.write(str(n-10) + reason)
			print(str(n-10))
		return n - 10
	else:
		recursions = recursions + 1
		reason = ' since {0!s} is equal to or less than 100\n'.format(n) 
		return mccarthy_verbose(mccarthy_verbose(n+11))

mccarthy_verbose(number)
