from quicksort import quick_sort
import re

class Version:

    def __init__(self,major,minor,patch):
        self.major = int(major)
        self.minor = int(minor)
        self.patch = int(patch)
        self.label = ''
        self.build = ''

    def __str__(self):
        value = '.'.join([`self.major`, `self.minor`, `self.patch`])
        if self.label:
            value += '-' + self.label
        if self.build:
            value += '+' + self.build
        return value

    def label(self,label):
        self.label = label

    def build(self,build):
        self.build = build

    def __lt__(self, other):
        if not other.major == self.major:
            return self.major < other.major
        elif not other.minor == self.minor:
            return self.minor < other.minor
        elif not other.patch == self.patch:
            return self.patch < other.patch
        elif self.label and not other.label:
            return True
        else:
            return False

    def __eq__(self, other):
        return not self<other and not other<self

    def __ne__(self, other):
        return self<other or other<self

    def __gt__(self, other):
        return other<self

    def __ge__(self, other):
        return not self<other

    def __le__(self, other):
        return not other<self

T = int(raw_input())

versions = []

for x in xrange(0,T):
    version = raw_input()
    versionlist = re.split(r'[\.\+\-]',version)
    versions.append(Version(versionlist[0], versionlist[1], versionlist[2]))
    if '-' in version:
        versions[-1].label = versionlist[3]
    if '+' in version:
        versions[-1].build = versionlist[-1]

versions = quick_sort(versions)

print 'Sorted Versions:'

for x in versions:
    print x
