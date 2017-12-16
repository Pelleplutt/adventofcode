import task

class dec16_1(task.str_task):
    def run_list(self, data):
        prg = list(data[0])
        line = data[1]

        for ins in line.split(','):
            if ins[0] == 's':
                count = int(ins[1:])
                l = prg[-count:]
                l.extend(prg[:-count])
                prg = l
            elif ins[0] == 'x':
                p1, p2 = ins[1:].split('/')
                p1 = int(p1)
                p2 = int(p2)
                p = prg[p1]
                prg[p1] = prg[p2]
                prg[p2] = p
            elif ins[0] == 'p':
                p1 = prg.index(ins[1])
                p2 = prg.index(ins[3])
                p = prg[p1]
                prg[p1] = prg[p2]
                prg[p2] = p

        return ''.join(prg)

class dec16_2(task.str_task):
    def danceit(self, prg, line):
        for ins in line.split(','):
            if ins[0] == 's':
                count = int(ins[1:])
                l2 = prg[-count:]
                l2.extend(prg[:-count])
                prg = l2
            elif ins[0] == 'x':
                p1, p2 = ins[1:].split('/')
                p1 = int(p1)
                p2 = int(p2)
                p = prg[p1]
                prg[p1] = prg[p2]
                prg[p2] = p
            elif ins[0] == 'p':
                p1 = prg.index(ins[1])
                p2 = prg.index(ins[3])
                p = prg[p1]
                prg[p1] = prg[p2]
                prg[p2] = p
        return prg

    def run_list(self, data):
        prg = list(data[0])
        line = data[1]

        loopidx = None
        for dance in range(1000):
            prg = self.danceit(prg, line)

            p = ''.join(prg)
            if p == data[0]:
                loopidx = dance + 1
                break

        prg = list(data[0])
        for dance in range(1000000000 % loopidx):
            prg = self.danceit(prg, line)

        return ''.join(prg)


if __name__ == "__main__":
    dec16_1().runtests()
    dec16_2().runtests()
