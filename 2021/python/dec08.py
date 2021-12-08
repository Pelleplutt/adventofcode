#!/usr/bin/env python3

import sys
import task

class Dec08a(task.StrTask):
    def run_list(self, data):
        total_count = 0
        for indata in data:
            entries = indata[indata.index(' | ') + 3:].split()

            for entry in entries:
                if len(entry) in (2, 3, 4, 7):
                    total_count += 1

        return total_count

class Dec08b(task.StrTask):
    """
    Numbers are:
    0 abc-efg
    1 --c--f-
    2 a-cd-fg
    3 a-cd-fg
    4 -bcd-f-
    5 ab-d-fg
    6 ab-defg
    7 a-c--f-
    8 abcdefg
    9 abcd-fg

    Pattern lengths
    2: 1
    3: 7
    4: 4
    5: 2, 3, 5
    6: 0, 6, 9
    7: 8
    """

    def run_list(self, data):
        total_sum = 0
        for indata in data:
            patterns = indata[:indata.index(' | ')].split()
            entries = indata[indata.index(' | ') + 3:].split()

            # integer to pattern number map, mapping actual number to offset in patterns
            patternmap = [-1] * 10

            for idx, pattern in enumerate(patterns):
                patterns[idx] = set(sorted(pattern))
            for idx, entry in enumerate(entries):
                entries[idx] = set(sorted(entry))

            # get the knowns
            for idx, pattern in enumerate(patterns):
                if len(pattern) == 2:
                    patternmap[1] = idx
                elif len(pattern) == 3:
                    patternmap[7] = idx
                elif len(pattern) == 4:
                    patternmap[4] = idx
                elif len(pattern) == 7:
                    patternmap[8] = idx

            for idx, pattern in enumerate(patterns):
                # 9 is the only with 100% overlap of 4 that is not 8
                if patterns[patternmap[4]] < pattern and idx != patternmap[8]:
                    patternmap[9] = idx

            for idx, pattern in enumerate(patterns):
                # 0 and 3 overlap 100% with 7, but 3 is len 5 and 0 is len 6
                # the only other doing this is 9
                if patterns[patternmap[7]] < pattern and idx != patternmap[9]:
                    if len(pattern) == 5:
                        patternmap[3] = idx
                    elif len(pattern) == 6:
                        patternmap[0] = idx

            for idx, pattern in enumerate(patterns):
                # overlap 2 and 4 is 2, overlap 5 and 4 is 3, both are len 5
                # and the only other len 5 is 3
                if len(pattern) == 5 and idx != patternmap[3]:
                    #pprint.pprint(pat[dmap[4]].intersection(p))
                    if len(patterns[patternmap[4]].intersection(pattern)) == 2:
                        patternmap[2] = idx
                    if len(patterns[patternmap[4]].intersection(pattern)) == 3:
                        patternmap[5] = idx

            for idx, pattern in enumerate(patterns):
                # 6 is the only len 6 char not identified so far,
                # 0 and 9 are the other two len 6
                if len(pattern) == 6 and idx not in (patternmap[0], patternmap[9]):
                    patternmap[6] = idx

            legend = {}
            for idx, pattern in enumerate(patternmap):
                sortedpattern = ''.join(sorted(patterns[pattern]))
                legend[sortedpattern] = idx

            rowsum = 0
            for entry in entries:
                pattern = ''.join(sorted(entry))
                rowsum = rowsum * 10 + legend[pattern]

            total_sum += rowsum

        return total_sum


if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec08a().run_tests_from_commandline()
        Dec08b().run_tests_from_commandline()
    else:
        Dec08a().runtests()
        Dec08b().runtests()
