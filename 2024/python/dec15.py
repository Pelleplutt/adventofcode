#!/usr/bin/env python3

import pprint
import sys
import task

class Dec15(task.Task):
    def _print_warehouse(self, warehouse):
        for row in warehouse:
            print(''.join(row))

    def run(self, data):
        warehouse, moves = data

        robotx, roboty = 0,0
        for y, row in enumerate(warehouse):
            for x, what in enumerate(row):
                if what == '@':
                    robotx = x
                    roboty = y
                    break
            if robotx > 0:
                break
        for move in moves:
            if self._move(warehouse, move, robotx, roboty):
                if move == '>':
                    robotx += 1
                elif move == 'v':
                    roboty += 1
                elif move == '<':
                    robotx -= 1
                elif move == '^':
                    roboty -= 1

        return self._gps_sum(warehouse)


class Dec15a(Dec15):
    def parse(self, rawdata):
        split = rawdata.index('')
        warehouse = []
        for rrow in rawdata[:split]:
            warehouse.append(list(rrow))
        moves = ''.join(rawdata[split:])

        return (warehouse, moves)
    
    def _move(self, warehouse, move, x, y):
        if move == '>':
            x += 1
        elif move == 'v':
            y += 1
        elif move == '<':
            x -= 1
        elif move == '^':
            y -= 1

        if warehouse[y][x] == '#':
            return False
        if warehouse[y][x] == 'O':
            if not self._move(warehouse, move, x, y):
                return False
        if warehouse[y][x] == '.':
            if move == '>':
                warehouse[y][x] = warehouse[y][x - 1]
                warehouse[y][x - 1] = '.'
            elif move == 'v':
                warehouse[y][x] = warehouse[y - 1][x]
                warehouse[y - 1][x] = '.'
            elif move == '<':
                warehouse[y][x] = warehouse[y][x + 1]
                warehouse[y][x + 1] = '.'
            elif move == '^':
                warehouse[y][x] = warehouse[y + 1][x]
                warehouse[y + 1][x] = '.'
            return True
        raise AssertionError(f"We failed at {x},{y}, move {move}")
    
    def _gps_sum(self, warehouse):
        sum = 0
        for y, row in enumerate(warehouse):
            for x, what in enumerate(row):
                if what == 'O':
                    sum += y * 100 + x
        return sum

class Dec15b(Dec15):
    def parse(self, rawdata):
        split = rawdata.index('')
        warehouse = []
        for rrow in rawdata[:split]:
            nrow = ''
            for chr in rrow:
                if chr == 'O':
                    nrow += '[]'
                elif chr == '@':
                    nrow += '@.'
                else:
                    nrow += chr + chr
    
            warehouse.append(list(nrow))
        moves = ''.join(rawdata[split:])

        return (warehouse, moves)

    # Call with left edge of box, will check if possible to move entire box up
    def _can_move(self, warehouse, move, x, y):
        yoffset = 0
        xoffset = 0
        if move == '^':
            yoffset = -1
        elif move == 'v':
            yoffset = 1
        elif move == '>':
            xoffset = 2
        elif move == '<':
            xoffset = -1
        else:
            raise AssertionError(f"Cannot probe move of type {move}")

        if yoffset:
            if warehouse[y + yoffset][x] == '#' or warehouse[y + yoffset][x + 1] == '#':
                return False

            if warehouse[y + yoffset][x] == '.' and warehouse[y + yoffset][x + 1] == '.':
                return True

            # []  []   []
            # []   [] []
            if warehouse[y + yoffset][x] == ']':
                if not self._can_move(warehouse, move, x - 1, y + yoffset):
                    return False
            if warehouse[y + yoffset][x] == '[':
                if not self._can_move(warehouse, move, x, y + yoffset):
                    return False
            if warehouse[y + yoffset][x + 1] == '[':
                if not self._can_move(warehouse, move, x + 1, y + yoffset):
                    return False
            
            return True

        if xoffset:
            if warehouse[y][x + xoffset] == '#':
                return False

            if warehouse[y][x + xoffset] == '.':
                return True
            
            if xoffset < 0 and warehouse[y][x - 1] == ']':
                return self._can_move(warehouse, move, x - 2, y)
            if xoffset > 0 and warehouse[y][x + 2] == '[':
                return self._can_move(warehouse, move, x + 2, y)

        raise AssertionError(f"We failed at {x},{y}, move {move}")

    def _move_cascading(self, warehouse, move, x, y):
        # We know this can be moved, just do it
        yoffset = 0
        xoffset = 0
        if move == '^':
            yoffset = -1
        elif move == 'v':
            yoffset = 1
        elif move == '>':
            xoffset = 2
        elif move == '<':
            xoffset = -2
        else:
            raise AssertionError(f"Cannot probe move of type {move}")

        if yoffset:
            if warehouse[y + yoffset][x] == ']':
                self._move_cascading(warehouse, move, x - 1, y + yoffset)
            if warehouse[y + yoffset][x] == '[':
                self._move_cascading(warehouse, move, x, y + yoffset)
            if warehouse[y + yoffset][x + 1] == '[':
                self._move_cascading(warehouse, move, x + 1, y + yoffset)
            warehouse[y][x] = '.'
            warehouse[y][x + 1] = '.'
            warehouse[y + yoffset][x] = '['
            warehouse[y + yoffset][x + 1] = ']'

        if xoffset:
            if warehouse[y][x + xoffset] == '[':
                self._move_cascading(warehouse, move, x + xoffset, y)

            if xoffset < 0:
                warehouse[y][x - 1] = '['
                warehouse[y][x] = ']'
                warehouse[y][x + 1] = '.'
            else:
                warehouse[y][x] = '.'
                warehouse[y][x + 1] = '['
                warehouse[y][x + 2] = ']'

    def _move(self, warehouse, move, x, y):
        yoffset = 0
        xoffset = 0
        if move == '^':
            yoffset = -1
        elif move == 'v':
            yoffset = 1
        elif move == '>':
            xoffset = 1
        elif move == '<':
            xoffset = -1
        else:
            raise AssertionError(f"Cannot probe move of type {move}")

        if yoffset:
            if warehouse[y + yoffset][x] == '#':
                return False
            if warehouse[y + yoffset][x] == '[':
                if not self._can_move(warehouse, move, x, y + yoffset):
                    return False
                self._move_cascading(warehouse, move, x, y + yoffset)
            if warehouse[y + yoffset][x] == ']':
                # Always call with left part of box
                if not self._can_move(warehouse, move, x - 1, y + yoffset):
                    return False
                self._move_cascading(warehouse, move, x - 1, y + yoffset)

            warehouse[y + yoffset][x] = '@'
            warehouse[y][x] = '.'
            return True
        elif xoffset:
            if warehouse[y][x + xoffset] == '#':
                return False
            if warehouse[y][x + xoffset] == '[': # this implies xoffset == 1
                if not self._can_move(warehouse, move, x + 1, y):
                    return False
                self._move_cascading(warehouse, move, x + 1, y)
            elif warehouse[y][x + xoffset] == ']': # this implies xoffset == -1
                # Always call with left part of box
                if not self._can_move(warehouse, move, x - 2, y):
                    return False
                self._move_cascading(warehouse, move, x - 2, y)

            warehouse[y][x + xoffset] = '@'
            warehouse[y][x] = '.'
            return True

        raise AssertionError(f"We failed at {x},{y}, move {move}")
    
    def _gps_sum(self, warehouse):
        sum = 0
        for y, row in enumerate(warehouse):
            for x, what in enumerate(row):
                if what == '[':
                    sum += y * 100 + x
        return sum

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec15a().run_specific_tests(sys.argv[1:])
        Dec15b().run_specific_tests(sys.argv[1:])
    else:
        Dec15a().runtests()
        Dec15b().runtests()
