#!/usr/bin/env python3

import task
import sys

class DecXXa(task.StrTask):
#class DecXXa(task.IntTask):
    """
    """
    def run(self, line):
        pass

    def run_list(self, data):
        pass

class DecXXb(task.StrTask):
#class DecXXb(task.IntTask):
    """
    """
    def run(self, line):
        pass

    def run_list(self, data):
        pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        DecXXa().run_tests_from_commandline()
        DecXXb().run_tests_from_commandline()
    else:
        DecXXa().runtests()
        DecXXb().runtests()
