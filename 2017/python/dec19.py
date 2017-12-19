import task

class dec19_1(task.str_task):
    def move(self, data, line, linepos, hv, pm):
        if hv == 'h':
            linepos += pm
        elif hv == 'v':
            line += pm
        l = data[line]
        c = l[linepos]

        return l, c, line, linepos

    def run_list(self, data):
        line = 0
        linepos = data[line].index('|')
        hv = 'v'
        pm = 1
        l = data[line]
        c = l[linepos]
        passed = []

        while c != ' ':
            if c == '-':
                hv = 'h'
                while c not in ('+', ' '):
                    l, c, line, linepos = self.move(data, line, linepos, hv, pm)
                    if c >= 'A' and c <= 'Z':
                        passed.append(c)
            elif c == '|':
                hv = 'v'
                while c not in ('+', ' '):
                    l, c, line, linepos = self.move(data, line, linepos, hv, pm)
                    if c >= 'A' and c <= 'Z':
                        passed.append(c)

            if c == '+':
                if hv == 'v':
                    if linepos + 1 < len(l) and (l[linepos + 1] in ('-', '+')  or l[linepos + 1].isalpha()):
                        hv = 'h'
                        pm = 1
                    elif linepos > 0 and (l[linepos - 1] in ('-', '+') or l[linepos - 1].isalpha()):
                        hv = 'h'
                        pm = -1
                    else:
                        raise Exception("Cannot corner hv={0} pm={1} c={2} line={3} linepos={4}".format(hv, pm, c, line, linepos))
                else:
                    if line + 1 < len(data) and (data[line + 1][linepos] in ('|', '+') or data[line + 1][linepos].isalpha()):
                        hv = 'v'
                        pm = 1
                    elif line > 0 and (data[line - 1][linepos] in ('|', '+') or data[line - 1][linepos].isalpha()):
                        hv = 'v'
                        pm = -1
                    else:
                        raise Exception("Cannot corner hv={0} pm={1} c={2} line={3} linepos={4}".format(hv, pm, c, line, linepos))
                l, c, line, linepos = self.move(data, line, linepos, hv, pm)

            if hv == 'v':
                while c >= 'A' and c <= 'Z':
                    passed.append(c)
                    l, c, line, linepos = self.move(data, line, linepos, hv, pm)
            elif hv == 'h':
                while c >= 'A' and c <= 'Z':
                    passed.append(c)
                    l, c, line, linepos = self.move(data, line, linepos, hv, pm)

        return ''.join(passed)


class dec19_2(task.str_task):
    def move(self, data, line, linepos, hv, pm):
        if hv == 'h':
            linepos += pm
        elif hv == 'v':
            line += pm
        l = data[line]
        c = l[linepos]

        return l, c, line, linepos

    def run_list(self, data):
        line = 0
        linepos = data[line].index('|')
        hv = 'v'
        pm = 1
        l = data[line]
        c = l[linepos]
        steps = 0

        while c != ' ':
            if c == '-':
                hv = 'h'
                while c not in ('+', ' '):
                    l, c, line, linepos = self.move(data, line, linepos, hv, pm)
                    steps += 1
            elif c == '|':
                hv = 'v'
                while c not in ('+', ' '):
                    l, c, line, linepos = self.move(data, line, linepos, hv, pm)
                    steps += 1

            if c == '+':
                if hv == 'v':
                    if linepos + 1 < len(l) and (l[linepos + 1] in ('-', '+')  or l[linepos + 1].isalpha()):
                        hv = 'h'
                        pm = 1
                    elif linepos > 0 and (l[linepos - 1] in ('-', '+') or l[linepos - 1].isalpha()):
                        hv = 'h'
                        pm = -1
                    else:
                        raise Exception("Cannot corner hv={0} pm={1} c={2} line={3} linepos={4}".format(hv, pm, c, line, linepos))
                else:
                    if line + 1 < len(data) and (data[line + 1][linepos] in ('|', '+') or data[line + 1][linepos].isalpha()):
                        hv = 'v'
                        pm = 1
                    elif line > 0 and (data[line - 1][linepos] in ('|', '+') or data[line - 1][linepos].isalpha()):
                        hv = 'v'
                        pm = -1
                    else:
                        raise Exception("Cannot corner hv={0} pm={1} c={2} line={3} linepos={4}".format(hv, pm, c, line, linepos))
                l, c, line, linepos = self.move(data, line, linepos, hv, pm)
                steps += 1

            if hv == 'v':
                while c.isalpha():
                    l, c, line, linepos = self.move(data, line, linepos, hv, pm)
                    steps += 1
            elif hv == 'h':
                while c.isalpha():
                    l, c, line, linepos = self.move(data, line, linepos, hv, pm)
                    steps += 1

        return steps

if __name__ == "__main__":
    dec19_1().runtests()
    dec19_2().runtests()
