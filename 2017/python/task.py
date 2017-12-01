import glob
import os.path
import sys

class testdata(object):
    def __init__(self, basename):
        self.basename = basename
        self.desc = os.path.split(basename)[1]
        self.load()

    def load(self):
        self.input = self.loadfile(self.basename + '.in')
        self.output = self.loadfile(self.basename + '.out')

    def loadfile(self, file):
        return open(file, 'r').readline().rstrip().rstrip()

class task(object):
    def __init__(self):
        self.testpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'tests', self.__class__.__name__)

    def runtests(self):
        for test in self.tests():
            out = self.run(test.input)
            if out != test.output:
                print("{0} NOT OK, got '{1}' expected '{2}'".format(test.desc, out, test.output))
            else:
                print("{0} OK".format(test.desc))

    def main(self):
        if len(sys.argv) > 1:
            for data in sys.argv[1:]:
                print("{0}: {1}".format(data, self.run(data)))
        else:
            self.runtests()

    def tests(self):
        for fil in sorted(glob.glob(os.path.join(self.testpath, '*.in'))):
            yield testdata(os.path.splitext(fil)[0])
