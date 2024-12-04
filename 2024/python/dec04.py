#!/usr/bin/env python3

import pprint
import sys
import task

class Dec04a(task.StrTask):
    xmas_tests = [
        ( 1,  0),
        (-1,  0),
        ( 0,  1),
        ( 0, -1),
        ( 1,  1),
        ( 1, -1),
        (-1,  1),
        (-1, -1),
    ]

    def _find_xmas_dir(self, data, xpos, ypos, maxx, maxy, xrel, yrel):

        yrand = ypos + yrel * 3
        xrand = xpos + xrel * 3

        if  xrand >= 0 and xrand + 1 <= maxx and \
            yrand >= 0 and yrand + 1 <= maxy and \
            data[ypos + yrel]    [xpos + xrel] == 'M' and \
            data[ypos + yrel * 2][xpos + xrel * 2] == 'A' and \
            data[ypos + yrel * 3][xpos + xrel * 3] == 'S':

                return 1

        return 0

    def run_list(self, data):
        count = 0
        maxx = len(data[0])
        maxy = len(data)
        for y in range(maxy):
            for x in range(maxx):
                if data[y][x] == 'X':
                    for xrel, yrel in Dec04a.xmas_tests:
                        count += self._find_xmas_dir(data, x, y, maxx, maxy, xrel, yrel)

        return count


class Dec04b(task.StrTask):
    def find_x_mas(self, data, xpos, ypos, maxx, maxy):
        if xpos + 3 <= maxx and ypos + 3 <= maxy:
            # M.S  S.S  M.M  S.M
            # .A.  .A.  .A.  .A.
            # M.S  M.M  S.S  S.M

            chrs = data[ypos][xpos] + data[ypos][xpos + 2] + \
                   data[ypos + 1][xpos + 1] + \
                   data[ypos + 2][xpos] + data[ypos + 2][xpos + 2]

            if chrs in ('MSAMS', 'SSAMM', 'MMASS', 'SMASM'):
                return 1
            
        return 0

    def run_list(self, data):
        count = 0
        maxx = len(data[0])
        maxy = len(data)
        for y in range(maxy):
            for x in range(maxx):
                count += self.find_x_mas(data, x, y, maxx, maxy)

        return count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec04a().run_tests_from_commandline()
        Dec04b().run_tests_from_commandline()
    else:
        Dec04a().runtests()
        Dec04b().runtests()
