import os.path
import glob

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

    def tests(self):
        for fil in sorted(glob.glob(os.path.join(self.testpath, '*.in'))):
            yield testdata(os.path.splitext(fil)[0])
