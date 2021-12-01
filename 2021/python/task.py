import glob
import os.path
import sys

def echoresult(input, result, maxlines=10):
    if input is not None:
        print("IN    : ", end='')
        if type(input) == list:
            print(input[0])
            for idx, line in enumerate(input[1:]):
                if maxlines is not None and idx > maxlines:
                    print("...")
                    break
                print("       ", line)
        else:
            print(input)

    print("RESULT: ", end='')
    if type(result) == list:
        print(result[0])
        for idx, line in enumerate(result[1:]):
            if maxlines is not None and idx > maxlines:
                print("...")
                break
            print("       " + line)
    else:
        print(result)

class TestData(object):
    def __init__(self, basename, in_int):
        self.basename = basename
        self.desc = os.path.split(basename)[1]
        self.load(in_int)

    def load(self, in_int):
        self.input = self.loadfile(self.basename + '.in', in_int)
        self.facit = self.loadfile(self.basename + '.out', False)

    def loadfile(self, file, integers):
        lines = []
        for line in open(file, 'r'):
            if integers:
                lines.append(int(line))
            else:
                lines.append(line.rstrip('\r\n'))
        return lines

    def resultok(self, result, facit):
        if len(result) != len(facit):
            return False
        for idx, line in enumerate(facit):
            if type(result[idx]) == int:
                line = int(line)
            if line != result[idx]:
                return False
        return True


    def run(self, task, echo=False):
        if "run_list" in dir(task):
            out = task.run_list(self.input)
        else:
            out = task.run(self.input[0])

        if type(out) != list:
            out = [out]

        if self.resultok(out, self.facit):
            if echo:
                echoresult(self.input, out)
            print("{0} OK".format(self.desc))
        else:
            echoresult(self.input, out)
            if len(self.facit):
                print("{0} NOT OK, expected".format(self.desc))
                echoresult(None, self.facit)
            else:
                print("{0} NOT OK".format(self.desc))


class Task(object):
    def __init__(self):
        self.testpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'tests', self.__class__.__name__)
        self.desc = self.__class__.__name__
        self.in_int = False
        self.init()

    def init(self):
        pass

    def runtest(self, name, echo=False):
        test = TestData(os.path.join(self.testpath, name), self.in_int)
        test.run(self, echo)

    def runtests(self, echo=False):
        print("{0}:".format(self.desc))
        for test in self.tests():
            test.run(self, echo)

    def tests(self):
        for fil in sorted(glob.glob(os.path.join(self.testpath, '*.in'))):
            yield TestData(os.path.splitext(fil)[0], self.in_int)

    # implement either
    # def run(self, line)
    # or
    # def run_list(self, data)


class IntTask(Task):
    def init(self):
        self.in_int = True


class StrTask(Task):
    pass
