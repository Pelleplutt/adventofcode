#!/usr/bin/env python3

import pprint
import sys
import task

class Dec09(task.Task):
    pass

class Dec09a(Dec09):
    def parse(self, rawdata):
        id = 0
        disk = []
        data = list(map(int, rawdata[0]))
        for n in range(int(len(data) / 2)):
            disk.extend([id] * data[2 * n])
            disk.extend([None] * data[2 * n + 1])
            id += 1

        if len(data) % 2:
            disk.extend([id] * data[-1])

        return disk

    def run(self, disk):
        lastblock = len(disk)

        for freepos in range(len(disk)):
            if lastblock < freepos:
                break

            if disk[freepos] is None:
                while lastblock > freepos:
                    lastblock -= 1
                    if disk[lastblock] is not None:
                        disk[freepos] = disk[lastblock]
                        disk[lastblock] = None
                        break

        checksum = 0
        for i in range(len(disk)):
            if disk[i] is not None:
                checksum += i * disk[i]

        return checksum




class Dec09b(Dec09):
    def parse(self, rawdata):
        id = 0
        disk = []
        data = list(map(int, rawdata[0]))
        for n in range(int(len(data) / 2)):
            # (id, fileblocks, freeblocks)
            disk.append([id, data[2*n], data[2*n + 1]])
            id += 1

        if len(data) % 2:
            disk.append([id, data[-1], 0])

        return disk

    def run(self, disk):
        moveblock = len(disk)
        while moveblock > 0:
            moveblock -= 1
            mid, mfileblocks, mfreeblocks = disk[moveblock]

            if mid is not None and mfileblocks:
                for targetblock in range(0, moveblock):
                    tid, tfileblocks, tfreeblocks = disk[targetblock]

                    if tfreeblocks >= mfileblocks:
                        disk[moveblock]  = [None, 0, mfileblocks + mfreeblocks]
                        disk.insert(targetblock + 1,
                                    [mid, mfileblocks, tfreeblocks - mfileblocks])
                        
                        # Index did not change since it is before the insert position
                        disk[targetblock][2] = 0

                        # Current index changes as we insert into array, compensate
                        moveblock += 1
                        break

        checksum = 0
        diskpos = 0
        for block in range(len(disk)):
            if disk[block][0] is not None:
                for fileblock in range(disk[block][1]):
                    checksum += (diskpos + fileblock) * disk[block][0]

            diskpos += disk[block][1] + disk[block][2]

        return checksum

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec09a().run_specific_tests(sys.argv[1:])
        Dec09b().run_specific_tests(sys.argv[1:])
    else:
        Dec09a().runtests()
        Dec09b().runtests()
