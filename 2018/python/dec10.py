import task
import re
import time

class dec10(task.StrTask):
    def field_print(self):
        minx = None
        miny = None
        maxx = None
        maxy = None

        dotpos = []
        for dot in self.dots:
            if minx is None or dot['x'] < minx:
                minx = dot['x']
            if maxx is None or dot['x'] > maxx:
                maxx = dot['x']
            if miny is None or dot['y'] < miny:
                miny = dot['y']
            if maxy is None or dot['y'] > maxy:
                maxy = dot['y']

            dotpos.append([dot['x'], dot['y']])

        if  maxx - minx > 100:
            return False
        dotpos.sort(key=lambda x: (x[1], x[0]))

        maxy += 1
        maxx += 1
        lasty = miny - 1
        lastx = minx - 1
        for dot in dotpos:
            x = dot[0]
            y = dot[1]

            if y > lasty:
                if lastx < maxx:
                    print('{}|'.format('.' * (maxx - lastx)))
                else:
                    print('|')
                
                for i in range(lasty + 1, y):
                    print('{}|'.format('.' * (maxx - minx + 1)))
                lasty = y
                lastx = minx - 1
            
            if x > lastx + 1:
                print('.' * (x - lastx - 1), end='')

            if lastx < x:
                lastx = x
                print('#', end='')

        if  maxx > lastx:
            print('{}|'.format('.' * (maxx - lastx)))
        else:
            print('|')

        return True

    def field_move(self):
        for dot in self.dots:
            dot['x'] += dot['xvel']
            dot['y'] += dot['yvel']            

    def run_list(self, data):
        self.dots = []
        for row in data:
            m = re.match('position=< *([0-9-]+), *([0-9-]+)> velocity=< *([0-9-]+), *([0-9-]+)>', row)
            self.dots.append({
                'x': int(m.group(1)),
                'y': int(m.group(2)),
                'xvel': int(m.group(3)),
                'yvel': int(m.group(4))
            })

        self.field_print()

        i = 0
        while True:
            i += 1
            self.field_move()
            if self.field_print():
                print(i)
                time.sleep(1)

if __name__ == "__main__":
    dec10().runtests()