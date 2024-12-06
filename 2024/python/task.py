import glob
import os
import os.path
import sys
import time

class TestData(object):
    def __init__(self, basename):
        self.basename = basename
        self.input_file = self.basename + '.in'
        self.output_file = self.basename + '.out'
        self.desc = os.path.split(basename)[1]
        self.facit = None
        self.input = None
        self.load()

    def load(self):
        try:
            if os.stat(self.input_file).st_size > 0:
                self.input = self._loadfile(self.input_file)
        except FileNotFoundError:
            raise AssertionError("No input found, file does not exist") from None

        if self.input and os.stat(self.output_file).st_size > 0:
            try:
                self.facit = self._loadfile(self.output_file)
            except FileNotFoundError:
                pass

    def _loadfile(self, file):
        lines = []
        for line in open(file, 'r'):
            lines.append(line.rstrip('\r\n'))
        return lines

    def run(self, task, echo=False):
        echoresult = True

        extra = ''
        if self.input:
            t0 = time.time()
            indata = task.parse(self.input.copy())
            t1 = time.time()
            out = task.run(indata)
            t2 = time.time()

            extra = f" ({((t1 - t0) * 1000):.2f} + {((t2 - t1) * 1000):.2f}ms)"

            if self.facit is None:
                status = '?'
            elif self._resultok(out, self.facit):
                status = 'OK'
                echoresult = False
            else:
                status = 'NOT OK'
                echoresult = True
        else:
            status = 'EMPTY'
            echoresult = False
            t0, t1 = 0, 0


        print(f" - {self.desc} {status}{extra}")
        if echoresult:
            echo = self._renderresult(out, self.facit)
            for e in echo:
                print('   ', e)

            print()

    def _resultok(self, result, facit):
        if type(result) == list:
            if len(result) != len(facit):
                return False
            for idx, line in enumerate(facit):
                if type(result[idx]) == int:
                    if not line.isnumeric():
                        return False
                    line = int(line)
                if line != result[idx]:
                    return False
        else:
            if len(facit) > 1:
                return False
            f = facit[0]
            if type(result) == int:
                if not f.isnumeric():
                    return False
                f = int(f)
            if result != f:
                return False

        return True

    def _renderresult(self, out, facit, maxlines=10):
        echo = []
        if type(out) == list:
            echo = self._renderresulttable(['Result', 'Expected'], [out, facit], maxcolwidth=40, maxlines=maxlines)
        elif out is None:
            echo.append(f"Result  : None")
            if facit is None:
                echo.append(f"Expected: None")
            else:
                if len(facit) > 1:
                    echo = self._renderresulttable(['Result', 'Expected'], [[out], facit], maxcolwidth=40, maxlines=maxlines)
                else:
                    echo.append(f"Expected: {facit[0]}")
        else:
            if facit is not None and len(facit) > 1:
                echo = self._renderresulttable(['Result', 'Expected'], [[out], facit], maxcolwidth=40, maxlines=maxlines)
            else:
                echo.append(f"Result  : {out}")
                if facit is not None:
                    echo.append(f"Expected: {facit[0]}")
        return echo

    def _renderresulttable(self, headers, columns, maxcolwidth=40, maxlines=None):
        echo = []
        colwidhts = []
        for i, col in enumerate(columns):
            cw = max(map(lambda x: len(str(x)) if x else 0, col))
            cw = max(cw, len(headers[i]))
            if maxcolwidth:
                cw = min(cw, maxcolwidth)
            
            colwidhts.append(cw)


        line = ''
        for i, head in enumerate(headers):
            cw = colwidhts[i]
            line += f"| {head.center(cw)} "
        echo.append(line + '|')
        
        line = ''
        for i, head in enumerate(headers):
            cw = colwidhts[i]
            line += f"+-{'-' * cw}-"
        echo.append(line + '+')

        row = 0
        while True:
            exhausted = True
            line = ''
            for i, head in enumerate(headers):
                cw = colwidhts[i]
                try:
                    s = str(columns[i][row]).ljust(cw)
                    if len(s) > maxcolwidth:
                        s = s[:maxcolwidth - 1] + '+'
                    line += f"| {s} "
                    exhausted = False
                except IndexError:
                    line += f"| {''.ljust(cw)} "
            if exhausted:
                break

            echo.append(line + '|')
            row += 1
            if row > maxlines:
                break

        line = ''
        for i, head in enumerate(headers):
            cw = colwidhts[i]
            line += f"+-{'-' * cw}-"
        echo.append(line + '+')
        return echo



class Task(object):
    def __init__(self):
        self.testpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'tests', self.__class__.__name__)
        self.desc = self.__class__.__name__

    def runtest(self, name, echo=False):
        test = TestData(os.path.join(self.testpath, name))
        test.run(self, echo)

    def runtests(self, echo=False):
        print(f"{self.desc}:")
        for test in self.tests():
            test.run(self, echo)

    def run_specific_tests(self, tests, echo=False):
        print(f"{self.desc}:")
        for name in tests:
            test = TestData(os.path.join(self.testpath, name))
            test.run(self, echo)

    def tests(self):
        for fil in sorted(glob.glob(os.path.join(self.testpath, '*.in'))):
            yield TestData(os.path.splitext(fil)[0])

    # implement these ########################################################
    def parse(self, data):
        return data

    def run(self, data):
        raise NotImplementedError("Missing run implementation")
