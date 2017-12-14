import task

class dec14_1(task.str_task):
    def rev(self, l, offset, length):
        elements = []
        for i in range(offset, offset + length):
            pos = i % len(l)
            elements.append(l[pos])
        for e in reversed(elements):
            l[offset] = e
            offset = (offset + 1) % len(l)

    def get_dh(self, data):
        lengths = list(map(lambda x: ord(x), list(data)))
        lengths.extend((17, 31, 73, 47, 23))
        l = list(range(0, 256))

        pos = 0
        skipsize = 0
        for i in range(0, 64):
            for length in lengths:
                if length > 255:
                    continue
                self.rev(l, pos, length)
                pos = (pos + length + skipsize) % 256
                skipsize = skipsize + 1

        dh = ''
        for i in range(0, 16):
            val = 0
            for v in l[(i * 16):(i * 16 + 16)]:
                val = val ^ v
            dh = dh + ("%0.2x" % val)

        return dh

    def run(self, data):
        used = 0
        for l in range(128):
            dh = self.get_dh("{0}-{1}".format(data, l))
            for d in list(dh):
                d = int('0x' + d, 16)
                for bitm in (8, 4, 2, 1):
                    if d & bitm > 0:
                        used += 1
        return used

class dec14_2(task.str_task):
    def rev(self, l, offset, length):
        elements = []
        for i in range(offset, offset + length):
            pos = i % len(l)
            elements.append(l[pos])
        for e in reversed(elements):
            l[offset] = e
            offset = (offset + 1) % len(l)

    def get_dh(self, data):
        lengths = list(map(lambda x: ord(x), list(data)))
        lengths.extend((17, 31, 73, 47, 23))
        l = list(range(0, 256))

        pos = 0
        skipsize = 0
        for i in range(0, 64):
            for length in lengths:
                if length > 255:
                    continue
                self.rev(l, pos, length)
                pos = (pos + length + skipsize) % 256
                skipsize = skipsize + 1

        dh = ''
        for i in range(0, 16):
            val = 0
            for v in l[(i * 16):(i * 16 + 16)]:
                val = val ^ v
            dh = dh + ("%0.2x" % val)

        return dh

    def expand_reg(self, lines, regions, lineno, pos, region):
        count = 0
        if lines[lineno][pos] == '#':
            if regions[lineno][pos] is None:
                count = 1
                regions[lineno][pos] = region
                if lineno > 0 and lines[lineno - 1][pos] == '#':
                    count += self.expand_reg(lines, regions, lineno - 1, pos, region)
                if lineno < 127 and lines[lineno + 1][pos] == '#':
                    count += self.expand_reg(lines, regions, lineno + 1, pos, region)
                if pos > 0 and lines[lineno][pos - 1] == '#':
                    count += self.expand_reg(lines, regions, lineno, pos - 1, region)
                if pos < 127 and lines[lineno][pos + 1] == '#':
                    count += self.expand_reg(lines, regions, lineno, pos + 1, region)
        return count

    def run(self, data):
        lines = []
        regions = []
        for l in range(128):
            dh = self.get_dh("{0}-{1}".format(data, l))
            mask = ''
            for d in list(dh):
                d = int('0x' + d, 16)
                for bitm in (8, 4, 2, 1):
                    if d & bitm > 0:
                        mask += '#'
                    else:
                        mask += '-'

            lines.append(mask)
            regions.append([None] * 128)

        lastregion = 0
        for lineno, line  in enumerate(lines):
            for pos in range(len(line)):
                if self.expand_reg(lines, regions, lineno, pos, lastregion) > 1:
                    lastregion += 1

        return lastregion

if __name__ == "__main__":
    dec14_1().runtests()
    dec14_2().runtests()
