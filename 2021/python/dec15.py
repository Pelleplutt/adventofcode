#!/usr/bin/env python3

import pprint
import sys
import task

class Dec15a(task.StrTask):
#class Dec15a(task.IntTask):
    """
    """
    def run(self, line):
        pass

    def run_list(self, data):
        pass

class Dec15b(task.StrTask):
#class Dec15b(task.IntTask):
    """
    """
    def run(self, line):
        pass

    def run_list(self, data):
        pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec15a().run_tests_from_commandline()
        Dec15b().run_tests_from_commandline()
    else:
        Dec15a().runtests()
        Dec15b().runtests()
