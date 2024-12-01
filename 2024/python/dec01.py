#!/usr/bin/env python3

import pprint
import sys
import task

class Dec01a(task.StrTask):
#class Dec01a(task.IntTask):
    """
    """
    def run(self, line):
        pass

    def run_list(self, data):
        pass

class Dec01b(task.StrTask):
#class Dec01b(task.IntTask):
    """
    """
    def run(self, line):
        pass

    def run_list(self, data):
        pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec01a().run_tests_from_commandline()
        Dec01b().run_tests_from_commandline()
    else:
        Dec01a().runtests()
        Dec01b().runtests()
