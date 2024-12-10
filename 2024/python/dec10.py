#!/usr/bin/env python3

import pprint
import sys
import task

class Dec10(task.Task):
    def parse(self, rawdata):
        data = []
        for row in rawdata:
            rd = []
            for col in row:
                 # Test data case only
                if col == '.':
                    rd.append(-99)
                else:
                    rd.append(int(col))
            data.append(rd)
        return data

class Dec10a(Dec10):
    def follow_trail(self, map, nines, head, xpos, ypos, maxx, maxy):
        if head == 9:
            nines.add(f"{xpos},{ypos}")
            return
        
        nhead = head + 1

        if ypos > 0 and map[ypos - 1][xpos] == nhead:
            self.follow_trail(map, nines, nhead, xpos, ypos - 1, maxx, maxy)
        if xpos > 0 and map[ypos][xpos - 1] == nhead:
            self.follow_trail(map, nines, nhead, xpos - 1, ypos, maxx, maxy)
        if ypos + 1 < maxy and map[ypos + 1][xpos] == nhead:
            self.follow_trail(map, nines, nhead, xpos, ypos + 1, maxx, maxy)
        if xpos + 1 < maxx and map[ypos][xpos + 1] == nhead:
            self.follow_trail(map, nines, nhead, xpos + 1, ypos, maxx, maxy)

    def run(self, map):
        trailheads = 0
        maxx = len(map[0])
        maxy = len(map)
        for ypos in range(maxy):
            for xpos, val in enumerate(map[ypos]):
                if val == 0:
                    nines = set()
                    self.follow_trail(map, nines, 0, xpos, ypos, maxx, maxy)
                    trailheads += len(nines)
                    
        return trailheads


class Dec10b(Dec10):
    def follow_trail(self, map, head, xpos, ypos, maxx, maxy):
        if head == 9:
            return 1
        
        nhead = head + 1
        score = 0

        if ypos > 0 and map[ypos - 1][xpos] == nhead:
            score += self.follow_trail(map, nhead, xpos, ypos - 1, maxx, maxy)
        if xpos > 0 and map[ypos][xpos - 1] == nhead:
            score +=  self.follow_trail(map, nhead, xpos - 1, ypos, maxx, maxy)
        if ypos + 1 < maxy and map[ypos + 1][xpos] == nhead:
            score += self.follow_trail(map, nhead, xpos, ypos + 1, maxx, maxy)
        if xpos + 1 < maxx and map[ypos][xpos + 1] == nhead:
            score += self.follow_trail(map, nhead, xpos + 1, ypos, maxx, maxy)

        return score

    def run(self, map):
        score = 0
        maxx = len(map[0])
        maxy = len(map)
        for ypos in range(maxy):
            for xpos, val in enumerate(map[ypos]):
                if val == 0:
                    score += self.follow_trail(map, 0, xpos, ypos, maxx, maxy)
                    
        return score

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec10a().run_specific_tests(sys.argv[1:])
        Dec10b().run_specific_tests(sys.argv[1:])
    else:
        Dec10a().runtests()
        Dec10b().runtests()
