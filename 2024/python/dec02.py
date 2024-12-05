#!/usr/bin/env python3

import pprint
import sys
import task

class Dec02(task.Task):
    def _is_safe(self, nums):
        diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

        for n in diffs:
            if (abs(n) < 1) or (abs(n) > 3) or (n > 0) != (diffs[0] > 0):
                return False
        return True

class Dec02a(Dec02):
    def run(self, data):
        count = 0
        for row in data:
            nums = list(map(lambda x: int(x), row.split()))
            if self._is_safe(nums):
                count += 1
        return count
            

class Dec02b(Dec02):
    def run(self, data):
        count = 0
        for row in data:
            nums = list(map(lambda x: int(x), row.split()))
            safe = self._is_safe(nums)

            if not safe:
                for skip in range(len(nums)):
                    if self._is_safe([nums[i] for i in range(len(nums)) if i != skip]):
                        safe = True
                        break

            if safe:
                count += 1
        return count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec02a().run_specific_tests(sys.argv[1:])
        Dec02b().run_specific_tests(sys.argv[1:])
    else:
        Dec02a().runtests()
        Dec02b().runtests()


#           6 8 9 10 12 13 12
# diffs:      2 1  1  2  1 -1
# not 0:        1  1  2  1 -1
# not 1:        3  1  2  1 -1
# not 2:      2    2  2  1 -1
# not 3:      2 2     3  1 -1
# not 4:      2 1  1     3 -1
# not 5:      2 1  1  2     0
# not 6:      2 1  1  2  1


#           84 86 88 90 93 97
# diffs:        2  2  2  3  4

