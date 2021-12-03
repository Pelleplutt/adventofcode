#!/usr/bin/env python3

import task

class dec01_1(task.IntTask):
    def run_list(self, data):
        incr = 0
        for (idx, d) in enumerate(data):
            if idx > 0 and data[idx -1] < d:
                incr += 1

        return incr

class dec01_2(task.IntTask):
    def run_list(self, data):
        incr = 0
        for i in range(0, len(data) - 3):
            if sum(data[i:i+3]) < sum(data[i + 1:i + 4]):
                incr += 1

        return incr

if __name__ == "__main__":
    dec01_1().runtests()
    dec01_2().runtests()