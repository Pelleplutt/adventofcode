import task

class dec23_1(task.str_task):
    def get_val(self, regs, arg):
        try:
            return int(arg)
        except:
            return regs.get(arg, 0)

    def run_list(self, lines):
        regs = {}
        ip = 0

        count = 0
        while ip < len(lines):
            instr, *a = lines[ip].split(' ')
            ipincr = 1

            if instr == 'set':
                regs[a[0]] = self.get_val(regs, a[1])
            elif instr == 'sub':
                regs[a[0]] = regs.get(a[0], 0) - self.get_val(regs, a[1])
            elif instr == 'mul':
                count += 1
                regs[a[0]] = regs.get(a[0], 0) * self.get_val(regs, a[1])
            elif instr == 'jnz' and self.get_val(regs, a[0]) != 0:
                ipincr = self.get_val(regs, a[1])

            ip += ipincr

        return count

class dec23_2(task.str_task):
    def python_org_code(self, lines):
        a = 1
        b = 67 * 100 + 100000
        c = b + 17000

        print("a=={0}, b=={1}, c=={2}".format(a, b, c))
        # a==1, b==106700, c==123700
        return 0

        while True:
            f = 1
            d = 2
            while True:
                e = 2
                while True:
                    if d * e == b:
                        f = 0
                    e += 1
                    if e == b:
                        break
                d += 1
                if d == b:
                    break
            if f == 0:
                h += 1

            if b == c:
                break
            b += 17

        return h

    def isprime(self, n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def run_list(self, lines):
        b = 106700
        h = 0
        while True:
            if self.isprime(b) == False:
                h += 1
            if b == 123700:
                break
            b += 17
        return h

if __name__ == "__main__":
    dec23_1().runtests()
    dec23_2().runtests()
