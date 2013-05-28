from sys import argv

def mccarthy_91(n):
	if n > 100:
		return n - 10
	else:
		return mccarthy_91(mccarthy_91(n+11))



print mccarthy_91(int(argv[1]))
