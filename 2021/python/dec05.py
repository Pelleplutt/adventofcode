#!/usr/bin/env python3

import task

class Line(object):
    def __init__(self, x1, y1, x2, y2):
        self.y1 = y1
        self.y2 = y2
        self.x1 = x1
        self.x2 = x2

    def draw(self, field):
        x = self.x1
        y = self.y1

        field[y][x] += 1

        while True:
            if x < self.x2:
                x += 1
            elif x > self.x2:
                x -= 1
            if y < self.y2:
                y += 1
            elif y > self.y2:
                y -= 1

            field[y][x] += 1

            if x == self.x2 and y == self.y2:
                break

class dec05_1(task.StrTask):
    """
    """
    def run_list(self, data):
        lines = []
        maxx, maxy = 0, 0

        for d in data:
            x1, y1, x2, y2 = map(int, d.replace(' -> ', ',').split(','))

            if x1 != x2 and y1 != y2:
                continue

            lines.append(Line(x1, y1, x2, y2))
            maxx = max(maxx, x1, x2)
            maxy = max(maxy, y1, y2)

        field = [[0] * (maxx + 1) for x in range(maxy + 1)]

        for line in lines:
            line.draw(field)

        count = 0
        for y in field:
            count += len(list(filter(lambda x: x > 1, y)))

        return count
        

class dec05_2(task.StrTask):
    """
    """

    def run_list(self, data):
        lines = []
        maxx, maxy = 0, 0

        for d in data:
            x1, y1, x2, y2 = map(int, d.replace(' -> ', ',').split(','))
            
            lines.append(Line(x1, y1, x2, y2))
            maxx = max(maxx, x1, x2)
            maxy = max(maxy, y1, y2)

        field = [[0] * (maxx + 1) for x in range(maxy + 1)]

        for line in lines:
            line.draw(field)

        count = 0
        for y in field:
            count += len(list(filter(lambda x: x > 1, y)))

        return count


if __name__ == "__main__":
    dec05_1().runtests()
    dec05_2().runtests()
