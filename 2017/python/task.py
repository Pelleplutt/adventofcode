import glob
import os.path
import sys

class testdata(object):
    def __init__(self, basename, in_multiline, out_multiline):
        self.basename = basename
        self.desc = os.path.split(basename)[1]
        self.load(in_multiline, out_multiline)

    def load(self, in_multiline, out_multiline):
        self.input = self.loadfile(self.basename + '.in', in_multiline)
        self.facit = self.loadfile(self.basename + '.out', out_multiline)

    def loadfile(self, file, multiline):
        if multiline:
            lines = []
            for line in open(file, 'r'):
                lines.append(line.rstrip())
            return lines
        else:
            return open(file, 'r').readline().rstrip()

    def resultok(self, result, facit):
        if len(result) != len(facit):
            return False
        for idx, line in enumerate(facit):
            if line != result[idx]:
                return False
        return True

    def echoresult(self, input, result):
        print("IN    : ", end='')
        if type(input) == list:
            print(input[0])
            for line in input[1:]:
                print("        " + line)
        else:
            print(input)

        print("RESULT: ", end='')
        if type(result) == list:
            print(result[0])
            for line in result[1:]:
                print("        " + line)
        else:
            print(result)

    def run(self, task, echo=False):
        out = task.run(self.input)
        if self.resultok(out, self.facit):
            if echo:
                self.echoresult(self.input, out)
            print("{0} OK".format(self.desc))
        else:
            self.echoresult(self.input, out)
            print("{0} NOT OK, expected".format(self.desc))
            self.echoresult(self.input, self.facit)


class task(object):
    in_multiline = False
    out_multiline = False

    def __init__(self):
        self.testpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'tests', self.__class__.__name__)
        self.desc = self.__class__.__name__
        self.init()

    def init(self):
        pass

    def runtest(self, name, echo=False):
        test = testdata(os.path.join(self.testpath, name), self.in_multiline, self.out_multiline)
        test.run(self, echo)

    def runtests(self, echo=False):
        print("{0}:".format(self.desc))
        for test in self.tests():
            test.run(self, echo)

    def main(self, echo=False):
        if len(sys.argv) > 1:
            for data in sys.argv[1:]:
                print("{0}: {1}".format(data, self.run(data)))
        else:
            self.runtests(echo)

    def tests(self):
        for fil in sorted(glob.glob(os.path.join(self.testpath, '*.in'))):
            yield testdata(os.path.splitext(fil)[0], self.in_multiline, self.out_multiline)
