#!/usr/bin/env python3

import pprint
import sys
import task

class Dec14(task.Task):
    def _draw(self, sizex, sizey, robots):
        field = []
        for y in range(sizey):
            field.append([0] * sizex)

        for robot in robots:
            x, y = robot[0]
            field[y][x] += 1

        s = ' 123456789ABCDEFGHIJKLMNOPQRSTUVXYZ'
        res = ''
        for y in range(sizey):
            res += ''.join(map(lambda x: s[x], field[y])) + '\n'
        return res

    def _count(self, robots, x1, y1, x2, y2):
        count = 0
        for robot in robots:
            if robot[0][0] >= x1 and \
               robot[0][0] < x2 and \
               robot[0][1] >= y1 and \
               robot[0][1] < y2:
                
                count += 1
        return count

    def parse(self, rawdata):
        robots = []
        sizex, sizey = map(int, rawdata[0].split(' '))
        for rrow in rawdata[1:]:
            p, v = rrow.split(' ')
            p = list(map(int, p[2:].split(',')))
            v = list(map(int, v[2:].split(',')))

            robots.append([p, v])
        return (sizex, sizey, robots)



class Dec14a(Dec14):

    def run(self, data):
        sizex, sizey, robots = data
        
        qx = int(sizex / 2)
        qy = int(sizey / 2)

        for iter in range(100):
            for rnum, robot in enumerate(robots):
                x, y = robot[0]
                vx, vy = robot[1]

                x = (x + vx) % sizex
                y = (y + vy) % sizey

                robots[rnum] = [[x, y],[vx, vy]]

        q1 = self._count(robots, 0, 0, qx, qy)
        q2 = self._count(robots, qx + 1, 0, 2 * qx + 1, qy)
        q3 = self._count(robots, 0, qy + 1, qx, 2 * qy + 1)
        q4 = self._count(robots, qx + 1, qy + 1, 2 * qx + 1, 2 * qy + 1)

        return q1 * q2 * q3 * q4


class Dec14b(Dec14):
    def run(self, data):
        sizex, sizey, robots = data
        qx = int(sizex / 2)
        qy = int(sizey / 2)

        min_dl = None
        min_dl_iter = None

        for iter in range(10000):
            for rnum, robot in enumerate(robots):
                x, y = robot[0]
                vx, vy = robot[1]

                x = (x + vx) % sizex
                y = (y + vy) % sizey

                robots[rnum] = [[x, y],[vx, vy]]
        
            q1 = self._count(robots, 0, 0, qx, qy)
            q2 = self._count(robots, qx + 1, 0, 2 * qx + 1, qy)
            q3 = self._count(robots, 0, qy + 1, qx, 2 * qy + 1)
            q4 = self._count(robots, qx + 1, qy + 1, 2 * qx + 1, 2 * qy + 1)

            if min_dl is None or q1 * q2 * q3 * q4 < min_dl:
                min_dl = q1 * q2 * q3 * q4
                min_dl_iter = iter + 1

        return min_dl_iter
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec14a().run_specific_tests(sys.argv[1:])
        Dec14b().run_specific_tests(sys.argv[1:])
    else:
        Dec14a().runtests()
        Dec14b().runtests()
