#!/usr/bin/env python3

import task
import sys
import pprint

class Dec07a(task.StrTask):
    """
    """
    def run(self, line):
        crabs = list(map(int, line.split(',')))

        min_cost = 0
        for align in range(max(crabs)):
            total_cost = 0
            for crab in crabs:
                total_cost += abs(crab - align)

            if min_cost == 0 or min_cost > total_cost:
                min_cost = total_cost
        return min_cost


class Dec07b(task.StrTask):
    """
    """
    def run(self, line):
        crabs = list(map(int, line.split(',')))

        costs = []
        acc_cost = 0
        for cost in range(max(crabs) + 1):
            acc_cost += cost
            costs += [acc_cost]

        min_cost = 0
        for align in range(max(crabs)):
            total_cost = 0
            for crab in crabs:
                total_cost += costs[abs(crab - align)]

            if min_cost == 0 or min_cost > total_cost:
                min_cost = total_cost
        return min_cost

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec07a().run_tests_from_commandline()
        Dec07b().run_tests_from_commandline()
    else:
        Dec07a().runtests()
        Dec07b().runtests()
