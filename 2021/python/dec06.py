#!/usr/bin/env python3

import sys
import task

class Dec06a(task.StrTask):
    def run(self, line):

        fish_list = list(map(int, line.split(',')))

        for day in range(80):
            for idx in range(len(fish_list)):
                if fish_list[idx] < 1:
                    fish_list[idx] = 6
                    fish_list += [8]
                else:
                    fish_list[idx] -= 1

        return len(fish_list)


class Dec06b(task.StrTask):
    def run(self, line):

        fish_list = [0] * 9
        for fish in line.split(','):
            fish_list[int(fish)] += 1

        for day in range(256):
            new_fish_cnt = fish_list.pop(0)
            fish_list[6] += new_fish_cnt
            fish_list.append(new_fish_cnt)

        total_fish = sum(fish_list)

        return total_fish

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec06a().run_tests_from_commandline()
        Dec06b().run_tests_from_commandline()
    else:
        Dec06a().runtests()
        Dec06b().runtests()
