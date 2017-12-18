import task

class dec18_1(task.str_task):
    def get_val(self, regs, arg):
        try:
            return int(arg)
        except:
            return regs.get(arg, 0)

    def run_list(self, data):
        regs = {}

        ofs = 0
        lsound = None
        while ofs < len(data):
            arg = data[ofs].split(' ')
            if len(arg) > 2:
                instr, a1, a2 = arg
            else:
                instr, a1 = arg
                a2 = None

            ofsmod = 1
            v1 = self.get_val(regs, a1)

            if instr == 'snd':
                lsound = v1
            elif instr == 'set':
                regs[a1] = self.get_val(regs, a2)
            elif instr == 'add':
                regs[a1] = regs.get(a1, 0) + self.get_val(regs, a2)
            elif instr == 'mul':
                regs[a1] = regs.get(a1, 0) * self.get_val(regs, a2)
            elif instr == 'mod':
                regs[a1] = regs.get(a1, 0) % self.get_val(regs, a2)
            elif instr == 'rcv' and v1 > 0:
                return lsound
            elif instr == 'jgz' and v1 > 0:
                ofsmod = self.get_val(regs, a2)

            ofs += ofsmod


class dec18_2(task.str_task):
    def get_val(self, regs, arg):
        try:
            return int(arg)
        except:
            return regs.get(arg, 0)

    def run_prg(self, data, regs, ofs, sent, sendstack, getstack):
        while ofs < len(data):
            arg = data[ofs].split(' ')
            if len(arg) > 2:
                instr, a1, a2 = arg
            else:
                instr, a1 = arg
                a2 = None

            ofsmod = 1
            v1 = self.get_val(regs, a1)

            if instr == 'snd':
                sendstack.append(v1)
                sent += 1
            elif instr == 'set':
                regs[a1] = self.get_val(regs, a2)
            elif instr == 'add':
                regs[a1] = regs.get(a1, 0) + self.get_val(regs, a2)
            elif instr == 'mul':
                regs[a1] = regs.get(a1, 0) * self.get_val(regs, a2)
            elif instr == 'mod':
                regs[a1] = regs.get(a1, 0) % self.get_val(regs, a2)
            elif instr == 'rcv':
                if len(getstack):
                    regs[a1] = getstack.pop(0)
                else:
                    return ofs, sent
            elif instr == 'jgz' and v1 > 0:
                ofsmod = self.get_val(regs, a2)

            ofs += ofsmod

        return -1, sent

    def run_list(self, data):
        r0 = {}
        r0['p'] = 0
        ofs0 = 0
        stack0 = []
        isent0 = 0

        r1 = {}
        r1['p'] = 1
        ofs1 = 0
        stack1 = []
        isent1 = 0

        while True:
            ofs0, isent0 = self.run_prg(data, r0, ofs0, isent0, stack1, stack0)

            if ofs0 < 0:
                return isent1
            else:
                ofs1, isent1 = self.run_prg(data, r1, ofs1, isent1, stack0, stack1)
                if ofs1 < 0:
                    return isent1

            if len(stack0) == 0 and len(stack1) == 0:
                return isent1


if __name__ == "__main__":
    dec18_1().runtests()
    dec18_2().runtests()
