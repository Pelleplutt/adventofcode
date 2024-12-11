#!/usr/bin/env python3

import pprint
import sys
import task
import math

class Dec11(task.Task):
    def _iter(self, stones):
        newstones = {}

        for stone in stones:
            if stone == 0:
                newstones[1] = newstones.get(1, 0) + stones[stone]
            elif int(math.log10(stone)) % 2 == 1:
                s = str(stone)
                l, r = int(s[:int(len(s) / 2)]), int(s[int(len(s) / 2):])

                newstones[l] = newstones.get(l, 0) + stones[stone]
                newstones[r] = newstones.get(r, 0) + stones[stone]
            else:
                newstone = stone * 2024
                newstones[newstone] = newstones.get(newstone, 0) + stones[stone]

        return newstones

    def _countstones(self, stones):
        count = 0
        for stone in stones:
            count += stones[stone]
        return count

    def parse(self, rawdata):
        stones = {}
        for stone in map(int, rawdata[0].split(' ')):
            stones[stone] = stones.get(stone, 0) + 1
        return stones

class Dec11a(Dec11):
    def run(self, stones):
        for i in range(25):
            stones = self._iter(stones)

        return self._countstones(stones)

class Dec11b(Dec11):
    def run(self, stones):
        for i in range(75):
            stones = self._iter(stones)

        return self._countstones(stones)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec11a().run_specific_tests(sys.argv[1:])
        Dec11b().run_specific_tests(sys.argv[1:])
    else:
        Dec11a().runtests()
        Dec11b().runtests()
