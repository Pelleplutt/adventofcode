#!/usr/bin/env python3

import task
class dec02_1(task.StrTask):
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
        
class dec02_2(task.StrTask):
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
    dec02_1().runtests()
    dec02_2().runtests()