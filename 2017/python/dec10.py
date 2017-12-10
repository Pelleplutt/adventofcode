import task

class dec10_1(task.str_task):
    def rev(self, l, offset, length):
        elements = []
        for i in range(offset, offset + length):
            pos = i % len(l)
            elements.append(l[pos])
        for e in reversed(elements):
            l[offset] = e
            offset = (offset + 1) % len(l)

    def run_list(self, data):
        listlen = int(data[0])
        lengths = map(lambda x: int(x), data[1].split(','))
        l = list(range(0, listlen))

        pos = 0
        skipsize = 0
        for length in lengths:
            if length > listlen - 1:
                continue
            self.rev(l, pos, length)
            pos = (pos + length + skipsize) % listlen
            skipsize = skipsize + 1

        return l[0] * l[1]

class dec10_2(task.str_task):
    def rev(self, l, offset, length):
        elements = []
        for i in range(offset, offset + length):
            pos = i % len(l)
            elements.append(l[pos])
        for e in reversed(elements):
            l[offset] = e
            offset = (offset + 1) % len(l)

    def run(self, data):
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


if __name__ == "__main__":
    dec10_1().runtests()
    dec10_2().runtests()
