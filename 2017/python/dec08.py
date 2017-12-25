import task
import re

class dec08_1(task.str_task):
    def run_list(self, data):
        regs = {}
        for line in data:
            m = re.match('^(.*) (dec|inc) (-?\d+) if (.*) (..?) (-?\d+)$', line)
            reg, do, val, condreg, condop, condarg = m.group(1, 2, 3, 4, 5, 6)
            condarg = int(condarg)
            val = int(val)
            if (
                (condop == '==' and regs.get(condreg, 0) == condarg) or
                (condop == '<=' and regs.get(condreg, 0) <= condarg) or
                (condop == '<'  and regs.get(condreg, 0) < condarg) or
                (condop == '>=' and regs.get(condreg, 0) >= condarg) or
                (condop == '>'  and regs.get(condreg, 0) > condarg) or
                (condop == '!=' and regs.get(condreg, 0) != condarg)):

                if do == 'inc':
                    regs[reg] = regs.get(reg, 0) + val
                elif do == 'dec':
                    regs[reg] = regs.get(reg, 0) - val

        max = None
        for val in regs.values():
            if max is None or val > max:
                max = val

        return max

class dec08_2(task.str_task):
    def run_list(self, data):
        regs = {}
        max = None
        for line in data:
            m = re.match('^(.*) (dec|inc) (-?\d+) if (.*) (..?) (-?\d+)$', line)
            reg, do, val, condreg, condop, condarg = m.group(1, 2, 3, 4, 5, 6)
            condarg = int(condarg)
            val = int(val)
            if (
                (condop == '==' and regs.get(condreg, 0) == condarg) or
                (condop == '<=' and regs.get(condreg, 0) <= condarg) or
                (condop == '<'  and regs.get(condreg, 0) < condarg) or
                (condop == '>=' and regs.get(condreg, 0) >= condarg) or
                (condop == '>'  and regs.get(condreg, 0) > condarg) or
                (condop == '!=' and regs.get(condreg, 0) != condarg)):

                if do == 'inc':
                    regs[reg] = regs.get(reg, 0) + val
                elif do == 'dec':
                    regs[reg] = regs.get(reg, 0) - val
                if max is None or regs[reg] > max:
                    max = regs[reg]
        return max

if __name__ == "__main__":
    dec08_1().runtests()
    dec08_2().runtests()
