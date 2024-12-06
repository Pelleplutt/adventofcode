#!/usr/bin/env python3

import pprint
import sys
import task

class Dec06(task.Task):
    def _move(self, field, row, col, direction, rowcount, colcount):
        peek = None
        if direction == 0 and row > 0:
            # UP
            peek = field[row - 1][col]
        elif direction == 1 and col + 1 < colcount:
            # RIGHT
            peek = field[row][col + 1]
        elif direction == 2 and row + 1 < rowcount:
            # DOWN
            peek = field[row + 1][col]
        elif direction == 3 and col > 0:
            # LEFT
            peek = field[row][col - 1]

        if peek is not None and peek == '#':
            return row, col, (direction + 1) % 4

        if direction == 0:
            # UP
            row -= 1
            if row < 0:
                return None, None, None
        elif direction == 1:
            # RIGHT
            col += 1
            if col >= colcount:
                return None, None, None
        elif direction == 2:
            # DOWN
            row += 1
            if row >= rowcount:
                return None, None, None
        elif direction == 3:
            # LEFT
            col -= 1
            if col < 0:
                return None, None, None

        return row, col, direction


class Dec06a(Dec06):
    def run(self, field):
        row, col, direction = 0, 0, 0

        rowcount = len(field)
        colcount = len(field[0])

        for row in range(rowcount):
            if '^' in field[row]:
                col = field[row].index('^')
                break

        visited = set()
        while direction is not None:
            visited.add(f"{row},{col}")
            row, col, direction = self._move(field, row, col, direction, rowcount, colcount)

        return len(visited)

class Dec06b(Dec06):
    def parse(self, rawdata):
        return list(map(list, rawdata))

    def _find_loop(self, field, row, col, direction, rowcount, colcount):
        visited_dir = set()
        while direction is not None:
            vkey = f"{row},{col},{direction}"
            if vkey in visited_dir:
                return True
            visited_dir.add(vkey)
            row, col, direction = self._move(field, row, col, direction, rowcount, colcount)
        return False

    def run(self, field):
        o_row, o_col, o_direction = 0, 0, 0
        rowcount = len(field)
        colcount = len(field[0])

        for o_row in range(rowcount):
            if '^' in field[o_row]:
                o_col = field[o_row].index('^')
                break

        # Only reasonable places to place an obstacle is where we walk so find vanilla walk through first
        row, col, direction = o_row, o_col, o_direction
        visited = set()
        while direction is not None:
            visited.add(f"{row},{col}")
            row, col, direction = self._move(field, row, col, direction, rowcount, colcount)

        loop_count = 0
        for v in visited:
            no_row, no_col = map(int, v.split(','))
            row, col, direction = o_row, o_col, o_direction
            if field[no_row][no_col] == '.':
                field[no_row][no_col] = '#'
                if self._find_loop(field, row, col, direction, rowcount, colcount):
                    loop_count += 1
                field[no_row][no_col] = '.'

        return loop_count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec06a().run_specific_tests(sys.argv[1:])
        Dec06b().run_specific_tests(sys.argv[1:])
    else:
        Dec06a().runtests()
        Dec06b().runtests()
