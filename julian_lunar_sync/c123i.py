from sys import argv

julian = int(argv[1].strip( ',' ))
lunar = int(argv[2])

julian_days = julian * 365 + (((julian / 4 * 10) - ((julian / 4 * 10) % 10)) / 10)
lunar_days = round(lunar * 29.53059)

if julian_days == lunar_days:
	print str(julian_days)
else:
	print 0
