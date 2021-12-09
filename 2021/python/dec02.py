#!/usr/bin/env python3

import sys
import task

class Dec02a(task.StrTask):
    def run_list(self, data):
        horiz = 0
        depth = 0
        
        for s in data:
            cmd, cnt = s.split(' ')
            cnt = int(cnt)

            if cmd == 'forward':
                horiz += cnt
            elif cmd == 'up':
                depth -= cnt
            elif cmd == 'down':
                depth += cnt

        return horiz * depth
        
class Dec02b(task.StrTask):
    def run_list(self, data):
        horiz = 0
        depth = 0
        aim = 0

        for s in data:
            cmd, cnt = s.split(' ')
            cnt = int(cnt)

            if cmd == 'forward':
                horiz += cnt
                depth += aim * cnt
            elif cmd == 'up':
                aim -= cnt
            elif cmd == 'down':
                aim += cnt

        return horiz * depth

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec02a().run_tests_from_commandline()
        Dec02b().run_tests_from_commandline()
    else:
        Dec02a().runtests()
        Dec02b().runtests()