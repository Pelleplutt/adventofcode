import task

class dec18_1(task.str_task):
    def get_val(self, regs, arg):
        try:
            return int(arg)
        except:
            return regs.get(arg, 0)

    def run_list(self, lines):
        regs = {}
        ip = 0
        lsound = None

        while ip < len(lines):
            instr, *a = lines[ip].split(' ')
            ipincr = 1

            if instr == 'snd':
                lsound = self.get_val(regs, a[0])
            elif instr == 'set':
                regs[a[0]] = self.get_val(regs, a[1])
            elif instr == 'add':
                regs[a[0]] = regs.get(a[0], 0) + self.get_val(regs, a[1])
            elif instr == 'mul':
                regs[a[0]] = regs.get(a[0], 0) * self.get_val(regs, a[1])
            elif instr == 'mod':
                regs[a[0]] = regs.get(a[0], 0) % self.get_val(regs, a[1])
            elif instr == 'rcv' and self.get_val(regs, a[0]) > 0:
                return lsound
            elif instr == 'jgz' and self.get_val(regs, a[0]) > 0:
                ipincr = self.get_val(regs, a[1])

            ip += ipincr

class dec18_2(task.str_task):
    def get_val(self, regs, arg):
        try:
            return int(arg)
        except:
            return regs.get(arg, 0)

    def run_prg(self, lines, regs, ip, sendcount, sendstack, getstack):
        while ip < len(lines):
            instr, *a = lines[ip].split(' ')
            ipincr = 1

            if instr == 'snd':
                sendstack.append(self.get_val(regs, a[0]))
                sendcount += 1
            elif instr == 'set':
                regs[a[0]] = self.get_val(regs, a[1])
            elif instr == 'add':
                regs[a[0]] = regs.get(a[0], 0) + self.get_val(regs, a[1])
            elif instr == 'mul':
                regs[a[0]] = regs.get(a[0], 0) * self.get_val(regs, a[1])
            elif instr == 'mod':
                regs[a[0]] = regs.get(a[0], 0) % self.get_val(regs, a[1])
            elif instr == 'rcv':
                if len(getstack):
                    regs[a[0]] = getstack.pop(0)
                else:
                    return ip, sendcount
            elif instr == 'jgz' and self.get_val(regs, a[0]) > 0:
                ipincr = self.get_val(regs, a[1])

            ip += ipincr

        return -1, sendcount

    def run_list(self, data):
        regs0 = {}
        regs0['p'] = 0
        ip0 = 0
        stack0 = []
        sendcount0 = 0

        regs1 = {}
        regs1['p'] = 1
        ip1 = 0
        stack1 = []
        sendcount1 = 0

        while True:
            ip0, sendcount0 = self.run_prg(data, regs0, ip0, sendcount0, stack1, stack0)
            ip1, sendcount1 = self.run_prg(data, regs1, ip1, sendcount1, stack0, stack1)

            if ip0 < 0 or ip1 < 0:
                return sendcount1

            if len(stack0) == 0 and len(stack1) == 0:
                return sendcount1


if __name__ == "__main__":
    dec18_1().runtests()
    dec18_2().runtests()
