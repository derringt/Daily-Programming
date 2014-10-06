from quicksort import quick_sort
from version import Version
import re

T = int(raw_input())

versions = []

for x in xrange(0,T):
    version = raw_input()
    versions.append(Version.fromstring(version))

versions = quick_sort(versions)

print 'Sorted Versions:'

for x in versions:
    print x
