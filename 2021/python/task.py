import glob
import os.path
import sys
import time

def echoresult(indata, result, maxlines=10):
    if indata is not None:
        print("IN    : ", end='')
        if type(indata) == list:
            print(indata[0])
            for idx, line in enumerate(indata[1:]):
                if maxlines is not None and idx > maxlines:
                    print("...")
                    break
                print(f"        {line}")
        else:
            print(indata)

    print("RESULT: ", end='')
    if type(result) == list:
        print(result[0])
        for idx, line in enumerate(result[1:]):
            if maxlines is not None and idx > maxlines:
                print("...")
                break
            print(f"      {line}")
    else:
        print(result)

class TestData(object):
    def __init__(self, basename, in_int):
        self.basename = basename
        self.desc = os.path.split(basename)[1]
        self.facit = None
        self.load(in_int)

    def load(self, in_int):
        self.input = self.loadfile(self.basename + '.in', in_int)
        try:
            self.facit = self.loadfile(self.basename + '.out', False)
        except FileNotFoundError:
            print("(No output found, facit is empty)")

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
        t0 = time.time()
        if "run_list" in dir(task):
            out = task.run_list(self.input.copy())
        else:
            out = task.run(self.input[0])
        t1 = time.time()

        if type(out) != list:
            out = [out]

        if self.facit is None:
            echoresult(self.input, out)
            print(f"{self.desc} ?")
        elif self.resultok(out, self.facit):
            if echo:
                echoresult(self.input, out)
            print(f"{self.desc} OK ({((t1 - t0) * 1000):.2f}ms)")
        else:
            echoresult(self.input, out)
            if len(self.facit):
                print(f"{self.desc} NOT OK, expected")
                echoresult(None, self.facit)
            else:
                print(f"{self.desc} NOT OK")


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
        print(f"{self.desc}:")
        for test in self.tests():
            test.run(self, echo)

    def run_tests_from_commandline(self, echo=False):
        print(f"{self.desc}:")
        for name in sys.argv[1:]:
            test = TestData(os.path.join(self.testpath, name), self.in_int)
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
