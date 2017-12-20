import task
import re

class dec20_1(task.str_task):
    def run_list(self, data):
        parts = []

        for line in data:
            vect = line.split(', ')
            part = {}
            for i in range(3):
                m = re.match('(.)=<(-?\d+),(-?\d+),(-?\d+)>', vect[i])
                part[m.group(1)] = [int(m.group(2)), int(m.group(3)), int(m.group(4))]

            parts.append(part)

        minp = None
        sizes = []

        for p in parts:
            asize = abs(p['a'][0]) + abs(p['a'][1]) + abs(p['a'][2])
            vsize = abs(p['v'][0]) + abs(p['v'][1]) + abs(p['v'][2])
            psize = abs(p['p'][0]) + abs(p['p'][1]) + abs(p['p'][2])
            sizes.append((psize, vsize, asize))

        for i, p in enumerate(sizes):
            if minp is None or (p[2] == sizes[minp][2] and p[1] == sizes[minp][1] and p[0] < sizes[minp][0]) or (p[2] == sizes[minp][2] and p[1] < sizes[minp][1]) or (p[2] < sizes[minp][2]):
                minp = i

        return minp


class dec20_2(task.str_task):
    def run_list(self, data):
        parts = []

        for line in data:
            vect = line.split(', ')
            part = {}
            for i in range(3):
                m = re.match('(.)=<(-?\d+),(-?\d+),(-?\d+)>', vect[i])
                part[m.group(1)] = [int(m.group(2)), int(m.group(3)), int(m.group(4))]

            parts.append(part)

        for loop in range(5000):
            pos = {}
            for i, p in enumerate(parts):
                if p is None:
                    continue
                p['v'] = [ p['v'][v] + p['a'][v] for v in range(3) ]
                p['p'] = [ p['p'][v] + p['v'][v] for v in range(3) ]

                pk = str(p['p'])
                if pos.get(pk) is not None:
                    parts[i] = None
                    parts[pos[pk]] = None
                else:
                    pos[pk] = i

        return len(parts) - parts.count(None)


if __name__ == "__main__":
    dec20_1().runtests()
    dec20_2().runtests()
