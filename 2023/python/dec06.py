#!/usr/bin/env python3

import pprint
import sys
import task

class Dec06a(task.StrTask):
    """
    """
    def run_list(self, data):
        durations = list(map(lambda x: int(x), data[0].split()[1:]))
        records = list(map(lambda x: int(x), data[1].split()[1:]))

        win_product = 1
        for race in range(len(durations)):
            race_wins = 0
            duration = durations[race]
            record = records[race]

            for i in range(duration):
                if (duration - i) * i > record:
                    race_wins += 1

            win_product *= race_wins

        return win_product


class Dec06b(task.StrTask):
#class Dec06b(task.IntTask):
    """
    """
    def run_list(self, data):
        duration = int(data[0].replace(' ', '').split(':')[1])
        record = int(data[1].replace(' ', '').split(':')[1])

        race_wins = 0

        for i in range(duration):
            if (duration - i) * i > record:
                race_wins += 1

        return race_wins

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec06a().run_tests_from_commandline()
        Dec06b().run_tests_from_commandline()
    else:
        Dec06a().runtests()
        Dec06b().runtests()
