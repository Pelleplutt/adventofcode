#!/usr/bin/env python3

import pprint
import re
import sys
import task

class Dec03(task.Task):
    pass

class Dec03a(Dec03):
    def run(self, data):
        sum = 0
        for s in data:
            matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', s)
            for m in matches:
                t1, t2 = m

                sum += int(t1) * int(t2)
        return sum

class Dec03b(Dec03):
    def run(self, data):
        sum = 0
        enable = True
        for s in data:
            matches = re.findall(r"(mul|do|don't)\(((\d{1,3}),(\d{1,3}))?\)", s)
            for m in matches:
                op, nop, t1, t2 = m
                if op == "do":
                    enable = True
                elif op == "don't":
                    enable = False
                elif op == "mul" and enable:
                    sum += int(t1) * int(t2)
        return sum

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec03a().run_specific_tests(sys.argv[1:])
        Dec03b().run_specific_tests(sys.argv[1:])
    else:
        Dec03a().runtests()
        Dec03b().runtests()
