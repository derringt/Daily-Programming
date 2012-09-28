from sys import argv

year_start = int(argv[1])
year_end = int(argv[2])

for x in range(year_start, year_end+1):
	if len(set(str(x))) == 4:
		print x
