#!/usr/bin/env python3

import sys
import task

class Dec09a(task.StrTask):
    """
    """
    def run_list(self, data):
        for idx, row in enumerate(data):
            data[idx] = list(map(int, row))

        high_y = len(data) - 1
        high_x = len(data[0]) - 1

        lowpoint_sum = 0
        for y in range(high_y + 1):
            for x, height in enumerate(data[y]):
                is_lowpoint = True

                if x > 0 and height >= data[y][x - 1]:
                    is_lowpoint = False
                if x < high_x and height >= data[y][x + 1]:
                    is_lowpoint = False
                if y > 0 and height >= data[y - 1][x]:
                    is_lowpoint = False
                if y < high_y and height >= data[y + 1][x]:
                    is_lowpoint = False

                if is_lowpoint:
                    lowpoint_sum += height + 1
        return lowpoint_sum


class Dec09b(task.StrTask):
    """
    """
    def expand(self, data, y, x, high_y, high_x):
        basin_size = 0
        if data[y][x] < 9:
            basin_size += 1
            data[y][x] = 9

            if x < high_x:
                basin_size += self.expand(data, y, x + 1, high_y, high_x)
            if x > 0:
                basin_size += self.expand(data, y, x - 1, high_y, high_x)
            if y < high_y:
                basin_size += self.expand(data, y + 1, x, high_y, high_x)
            if y > 0:
                basin_size += self.expand(data, y - 1, x, high_y, high_x)

        return basin_size


    def run_list(self, data):
        for idx, row in enumerate(data):
            data[idx] = list(map(int, row))

        high_y = len(data) - 1
        high_x = len(data[0]) - 1

        basins = []
        y = 0
        while y < high_y:
            x = 0
            while x < high_x:
                basin = self.expand(data, y, x, high_y, high_x)
                if basin > 0:
                    basins.append(basin)
                x += 1
            y += 1

        basins = sorted(basins)
        return basins[-1] * basins[-2] * basins[-3]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec09a().run_tests_from_commandline()
        Dec09b().run_tests_from_commandline()
    else:
        Dec09a().runtests()
        Dec09b().runtests()
