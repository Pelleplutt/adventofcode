#!/usr/bin/env python3

import pprint
import sys
import task

TRANSFORMATIONS =[
        [(0, 1), (1, 1), (2, 1)], 
        [(1, 1), (2, 1), (0, 1)], 
        [(2, 1), (0, 1), (1, 1)], 
        [(0, -1), (1, -1), (2, 1)], 
        [(1, -1), (2, -1), (0, 1)], 
        [(2, -1), (0, -1), (1, 1)], 
        [(0, -1), (1, 1), (2, -1)], 
        [(1, -1), (2, 1), (0, -1)], 
        [(2, -1), (0, 1), (1, -1)], 
        [(0, 1), (1, -1), (2, -1)], 
        [(1, 1), (2, -1), (0, -1)], 
        [(2, 1), (0, -1), (1, -1)],
        [(1, 1), (0, 1), (2, -1)], 
        [(0, 1), (2, -1), (1, 1)], 
        [(2, -1), (1, 1), (0, 1)], 
        [(1, -1), (0, -1), (2, -1)], 
        [(0, -1), (2, 1), (1, 1)], 
        [(2, 1), (1, -1), (0, 1)], 
        [(1, -1), (0, 1), (2, 1)], 
        [(0, -1), (2, -1), (1, -1)], 
        [(2, 1), (1, 1), (0, -1)], 
        [(1, 1), (0, -1), (2, 1)], 
        [(0, 1), (2, 1), (1, -1)], 
        [(2, -1), (1, -1), (0, -1)]
        ]

def findscannerrelativepositions(scannerdata):
    positions = [None] * len(scannerdata)
    positions[0] = [0, 0, 0] 

    found= set([0])
    notfound = set(range(1, len(scannerdata)))

    while notfound:
        scanner1 = found.pop()

        scanner1beacons = set()
        for b in scannerdata[scanner1]:
            scanner1beacons.add(tuple(b))

        found_now = set()
        for scanner2 in notfound:
            foundoverlap = False
            for transformation in TRANSFORMATIONS:
                transformed = []
                for beacon in scannerdata[scanner2]:
                    transformed.append([beacon[transformation[0][0]] * transformation[0][1],
                                        beacon[transformation[1][0]] * transformation[1][1],
                                        beacon[transformation[2][0]] * transformation[2][1]])

                for beacon1 in scannerdata[scanner1]:
                    for beacon2 in transformed:
                        x = beacon1[0] - beacon2[0]
                        y = beacon1[1] - beacon2[1]
                        z = beacon1[2] - beacon2[2]

                        scanner2beacons = set()
                        for b in transformed:
                            scanner2beacons.add(tuple([b[0] + x, b[1] + y, b[2] + z]))

                        if len(scanner2beacons.intersection(scanner1beacons)) >= 12:
                            found_now.add(scanner2)

                            scannerdata[scanner2] = list(scanner2beacons)
                            positions[scanner2] = (x, y, z)
                            foundoverlap = True
                            break
                    if foundoverlap:
                        break
                if foundoverlap:
                    break
        found |= found_now
        notfound -= found_now

    return positions


class Dec19a(task.StrTask):
    """
    """
    def run_list(self, data):
        scanner = -1
        scannerdata = []
        for d in data:
            if d[0:3] == '---':
                scanner = int(d[11:13].rstrip())
                scannerdata.append([])
            elif len(d):
                x, y, z = list(map(int, d.split(',')))
                scannerdata[-1].append([x, y, z])

        findscannerrelativepositions(scannerdata)

        allpoints = set()
        for scannerbeacons in scannerdata:
            for beacon in scannerbeacons:
                allpoints.add(tuple(beacon))

        return len(allpoints)

class Dec19b(task.StrTask):
    """
    """
    def run_list(self, data):
        scanner = -1
        scannerdata = []
        for d in data:
            if d[0:3] == '---':
                scanner = int(d[11:13].rstrip())
                scannerdata.append([])
            elif len(d):
                x, y, z = list(map(int, d.split(',')))
                scannerdata[-1].append([x, y, z])

        positions = findscannerrelativepositions(scannerdata)

        maxdistance = 0
        for i in positions:
            for j in positions:
                maxdistance = max(maxdistance, abs(i[0] - j[0]) + abs(i[1] - j[1]) + abs(i[2] - j[2]))
        return maxdistance


if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec19a().run_tests_from_commandline()
        Dec19b().run_tests_from_commandline()
    else:
        Dec19a().runtests()
        Dec19b().runtests()
