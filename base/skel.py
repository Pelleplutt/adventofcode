#!/usr/bin/env python3

import pprint
import sys
import task

class DecXX(task.Task):
    #def parse(self, rawdata):
    #    pass
    pass

class DecXXa(DecXX):
    def run(self, data):
        pass

class DecXXb(DecXX):
    def run(self, data):
        pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        DecXXa().run_specific_tests(sys.argv[1:])
        DecXXb().run_specific_tests(sys.argv[1:])
    else:
        DecXXa().runtests()
        DecXXb().runtests()
