#!/usr/bin/env python3

import sys
import task

PEEKS =  [
    [-1, -1], [-1,  0], [-1,  1],
    [ 0, -1],           [ 0,  1],
    [ 1, -1], [ 1,  0], [ 1,  1],
]

def flash_cell(data, x, y):
    flashes = 1
    data[y][x] = 0

    for peek in PEEKS:
        if y + peek[0] >= 0 and y + peek[0] < 10 and x + peek[1] >= 0 and x + peek[1] < 10:
            if data[y + peek[0]][x + peek[1]] > 0:
                data[y + peek[0]][x + peek[1]] += 1
            if data[y + peek[0]][x + peek[1]] > 9:
                flashes += flash_cell(data, x + peek[1], y + peek[0])

    return flashes

class Dec11a(task.StrTask):
    """
    """
    def run_list(self, data):
        for idx, octupuses in enumerate(data):
            data[idx] = list(map(int, octupuses))

        total_flashes = 0
        for step in range(100):
            for idx, octupuses in enumerate(data):
                data[idx] = list(map(lambda x: x + 1, octupuses))

            while True:
                flashes = 0
                for y, octupuses in enumerate(data):
                    for x, octopus in enumerate(octupuses):
                        if octopus > 9:
                            flashes += flash_cell(data, x, y)

                if flashes == 0:
                    break
                total_flashes += flashes

        return total_flashes

class Dec11b(task.StrTask):
    """
    """
    def run_list(self, data):
        for idx, octupuses in enumerate(data):
            data[idx] = list(map(int, octupuses))

        loop = 0
        while True:
            loop += 1
            total_flashes = 0

            for idx, octupuses in enumerate(data):
                data[idx] = list(map(lambda x: x + 1, octupuses))

            while True:
                flashes = 0
                for y, octupuses in enumerate(data):
                    for x, octopus in enumerate(octupuses):
                        if octopus > 9:
                            flashes += flash_cell(data, x, y)

                if flashes == 0:
                    break
                total_flashes += flashes

            if total_flashes == 100:
                return loop

        return 0

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec11a().run_tests_from_commandline()
        Dec11b().run_tests_from_commandline()
    else:
        Dec11a().runtests()
        Dec11b().runtests()
