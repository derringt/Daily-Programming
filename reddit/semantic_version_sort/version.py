import re

class Version:

    def __init__(self,major,minor,patch,label='',build=''):
        self.major = major
        self.minor = minor
        self.patch = patch
        self.label = label
        self.build = build

    @classmethod
    def fromstring(cls, versionstring):
        versionlist = re.split(r'[\.\+\-]',versionstring)
        new = cls(versionlist[0], versionlist[1], versionlist[2])
        if '-' in versionstring:
            new.label = versionlist[3]
        if '+' in versionstring:
            new.build = versionlist[-1]
        return new

    def __str__(self):
        value = '.'.join([self.major, self.minor, self.patch])
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
            return int(self.major) < int(other.major)
        elif not other.minor == self.minor:
            return int(self.minor) < int(other.minor)
        elif not other.patch == self.patch:
            return int(self.patch) < int(other.patch)
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
