#!/usr/bin/env python3

import pprint

import task
class dec03_1(task.StrTask):
    def run_list(self, data):
        gamma = 0        
        ones = [0] * len(data[0])

        for d in data:
            for idx, c in enumerate(d):
                if c == '1':
                    ones[idx] += 1

        pivot = len(data) / 2
        for i in ones:
            gamma = gamma << 1
            if i > pivot:
                gamma += 1

        epsilon = gamma ^ (2 ** len(ones) - 1)

        return gamma * epsilon        

class dec03_2(task.StrTask):
    def filter_pos(self, most_common, pos, data):
        count_ones = 0
        for d in data:
            if d[pos] == '1':
                count_ones += 1

        count_ones -= len(data) / 2
        filter_c = '0'
        if most_common == True:
            if count_ones > 0:
                filter_c = '1'
            elif count_ones == 0:
                filter_c = '1'
        elif count_ones < 0:
                filter_c = '1'

        return list(filter(lambda s: s[pos] == filter_c, data))

    def run_list(self, data):
        oxygen = data
        co2 = data
        for i in range(0, len(data[0])):
            oxygen = self.filter_pos(True, i, oxygen)

            if len(oxygen) == 1:
                break
        
        for i in range(0, len(data[0])):
            co2 = self.filter_pos(False, i, co2)

            if len(co2) == 1:
                break

        return int(oxygen[0], 2) * int(co2[0], 2)

if __name__ == "__main__":
    dec03_1().runtests()
    dec03_2().runtests()
