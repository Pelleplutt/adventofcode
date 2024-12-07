#!/usr/bin/env python3

import pprint
import sys
import task
import math

class Dec07(task.Task):
    def parse(self, rawdata):
        data = []
        for rd in rawdata:
            tv, nums = rd.split(':')
            nums = list(map(int, nums[1:].split(' ')))
            tv = int(tv)
            data.append([tv, nums])
        return data

    def run(self, data):
        sum = 0
        for tv, nums in data:
            if self._test(tv, nums):
                sum += tv

        return sum

class Dec07a(Dec07):
    def _test(self, tv, nums):
        alts = [nums[0]]
        for i, n in enumerate(nums[1:], start=1):
            nalts = []
            for a in alts:
                for na in [a * n, a + n]:
                    if na < tv:
                        nalts.append(na)
                    elif na == tv:
                        if i + 1 == len(nums):
                            return True
                        nalts.append(na)
            alts = nalts

        return False


class Dec07b(Dec07):
    def _test(self, tv, nums):
        alts = [nums[0]]
        for i, n in enumerate(nums[1:], start=1):
            nalts = []
            for a in alts:
                for na in [a * n, a + n, a * (math.pow(10, 1 + int(math.log10(n)))) + n]:
                    if na < tv:
                        nalts.append(na)
                    elif na == tv:
                        if i + 1 == len(nums):
                            return True
                        nalts.append(na)
            alts = nalts

        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec07a().run_specific_tests(sys.argv[1:])
        Dec07b().run_specific_tests(sys.argv[1:])
    else:
        Dec07a().runtests()
        Dec07b().runtests()
