import task
import re
import pprint

class Dec03_1(task.StrTask):
    def run_list(self, data):
        plist = []
        msize = 0
        for l in data:
            m = re.match('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', l)
            x = int(m.group(2))
            y = int(m.group(3))
            w = int(m.group(4))
            h = int(m.group(5))
            plist.append({
                'id': int(m.group(1)),
                'x': x,
                'y': y,
                'w': w,
                'h': h
            })
            if x+w > msize:
                msize = x+w

            if y+h > msize:
                msize = y+h

        fabric = []
        for i in range(0, msize):
            fabric.append([-1] * msize)
        overlaps = 0
        for p in plist:
            for y in (range(p['y'], p['y'] + p['h'])):
                for x in range(p['x'], p['x'] + p['w']):
                    if fabric[y][x] == -1:
                        fabric[y][x] = p['id']
                    elif fabric[y][x] == -2:
                        pass
                    else:
                        overlaps += 1
                        fabric[y][x] = -2
        return overlaps
        

class Dec03_2(task.StrTask):
    def run_list(self, data):
        plist = []
        msize = 0
        for l in data:
            m = re.match('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', l)
            x = int(m.group(2))
            y = int(m.group(3))
            w = int(m.group(4))
            h = int(m.group(5))
            plist.append({
                'id': int(m.group(1)),
                'x': x,
                'y': y,
                'w': w,
                'h': h
            })
            if x+w > msize:
                msize = x+w

            if y+h > msize:
                msize = y+h

        fabric = []
        for i in range(0, msize):
            fabric.append([-1] * msize)
        for p in plist:
            for y in (range(p['y'], p['y'] + p['h'])):
                for x in range(p['x'], p['x'] + p['w']):
                    if fabric[y][x] == -1:
                        fabric[y][x] = p['id']
                    elif fabric[y][x] == -2:
                        pass
                    else:
                        fabric[y][x] = -2

        for p in plist:
            dup = 0
            for y in (range(p['y'], p['y'] + p['h'])):
                for x in range(p['x'], p['x'] + p['w']):
                    if fabric[y][x] != p['id']:
                        dup = 1
                        break
                if dup > 0:
                    break

            if dup == 0:
                return p['id']




if __name__ == "__main__":
    dec03_1().runtests()
    dec03_2().runtests()
