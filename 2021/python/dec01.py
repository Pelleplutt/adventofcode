#!/usr/bin/env python3

import sys
import task

class Dec01a(task.IntTask):
    def run_list(self, data):
        incr = 0
        for (idx, d) in enumerate(data):
            if idx > 0 and data[idx -1] < d:
                incr += 1

        return incr

class Dec01b(task.IntTask):
    def run_list(self, data):
        incr = 0
        for i in range(0, len(data) - 3):
            if sum(data[i:i+3]) < sum(data[i + 1:i + 4]):
                incr += 1

        return incr

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec01a().run_tests_from_commandline()
        Dec01b().run_tests_from_commandline()
    else:
        Dec01a().runtests()
        Dec01b().runtests()
