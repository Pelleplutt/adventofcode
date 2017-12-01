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

    def run(self, task, echo=False):
        out = task.run(self.input)
        if echo:
            print("{0}: {1}".format(self.input, task.run(out)))
        if out != self.output:
            if echo:
                print("{0} NOT OK, expected '{2}'".format(self.desc, self.output))
            else:
                print("{0} NOT OK, got '{1}' expected '{2}'".format(self.desc, out, self.output))
        else:
            print("{0} OK".format(self.desc))


class task(object):
    def __init__(self):
        self.testpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'tests', self.__class__.__name__)

    def runtest(self, name, echo=False):
        test = testdata(os.path.join(self.testpath, name))
        test.run(self, echo)

    def runtests(self, echo=False):
        for test in self.tests():
            test.run(self, echo)

    def main(self):
        if len(sys.argv) > 1:
            for data in sys.argv[1:]:
                print("{0}: {1}".format(data, self.run(data)))
        else:
            self.runtests()

    def tests(self):
        for fil in sorted(glob.glob(os.path.join(self.testpath, '*.in'))):
            yield testdata(os.path.splitext(fil)[0])
