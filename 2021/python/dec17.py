#!/usr/bin/env python3

import sys
import task

def getxstepsinrange(speedfrom, speedto, maxsteps, xfrom, xto):
    xstepsinrange = []
    for startxvelocity in range(speedfrom, speedto):
        xvelocity = startxvelocity
        inrange = set()
        x = 0
        for step in range(maxsteps):
            x += xvelocity
            if xvelocity > 0:
                xvelocity -= 1
            elif xvelocity < 0:
                xvelocity += 1
            if x >= xfrom and x <= xto:
                inrange.add(step)
            if x > xto:
                break
        xstepsinrange.append(inrange)
    return xstepsinrange

def getystepsinrange(speedfrom, speedto, maxsteps, yfrom, yto):
    ystepsinrange = []
    ystepsmaxy = []

    for startyvelocity in range(speedfrom, speedto):
        yvelocity = startyvelocity
        localmaxy = 0
        inrange = set()
        y = 0
        for step in range(maxsteps):
            y += yvelocity
            yvelocity -= 1

            if y > localmaxy:
                localmaxy = y
            if y <= yto and y >= yfrom:
                inrange.add(step)

            if y < yfrom:
                break

        ystepsinrange.append(inrange)
        ystepsmaxy.append(localmaxy)

    return ystepsinrange, ystepsmaxy


class Dec17a(task.StrTask):
    """
    """
    def run(self, line):
        xfrom, xto = list(map(int, line[2:line.index(',')].split('..')))
        yfrom, yto = list(map(int, line[line.index(',') + 4:].split('..')))

        speedfrom = min(yfrom, xfrom) - 1
        speedto = max(xto, yto) + 1
        maxsteps = speedto

        xstepsinrange = getxstepsinrange(speedfrom, speedto, maxsteps, xfrom, xto)
        ystepsinrange, ystepsmaxy = getystepsinrange(speedfrom, speedto, maxsteps, yfrom, yto)

        maxy = 0
        for startxvelocity in range(speedfrom, speedto):
            for startyvelocity in range(speedfrom, speedto):
                if xstepsinrange[startxvelocity] & ystepsinrange[startyvelocity]:
                    if ystepsmaxy[startyvelocity] > maxy:
                        maxy = ystepsmaxy[startyvelocity]

        return maxy

class Dec17b(task.StrTask):
    """
    """
    def run(self, line):
        xfrom, xto = list(map(int, line[2:line.index(',')].split('..')))
        yfrom, yto = list(map(int, line[line.index(',') + 4:].split('..')))

        speedfrom = min(yfrom, xfrom) - 1
        speedto = max(xto, yto) + 1
        maxsteps = speedto

        xstepsinrange = getxstepsinrange(speedfrom, speedto, maxsteps, xfrom, xto)
        ystepsinrange, ystepsmaxy = getystepsinrange(speedfrom, speedto, maxsteps, yfrom, yto)

        count = 0
        for startxvelocity in range(speedfrom, speedto):
            for startyvelocity in range(speedfrom, speedto):
                if xstepsinrange[startxvelocity] & ystepsinrange[startyvelocity]:
                    count += 1

        return count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec17a().run_tests_from_commandline()
        Dec17b().run_tests_from_commandline()
    else:
        Dec17a().runtests()
        Dec17b().runtests()
