import task

class dec17_1(task.int_task):
    def run(self, steps):
        b = [0]
        pos = 0
        lenb = 1
        for i in range(1, 2017 + 1):
            pos = (pos + steps) % lenb
            pos = pos + 1
            if pos < lenb:
                b.insert(pos, i)
            else:
                b.append(i)
            lenb += 1

        return b[(pos + 1) % lenb]

class dec17_2(task.int_task):
    def run(self, steps):
        pos = 0
        after0 = 0
        before0 = 0
        for i in range(1, 50000000 + 1):
            pos = ((pos + steps) % (before0 + 1 + after0)) + 1

            if pos == (before0 + 1):
                after_num = i
                after0 += 1
            elif pos > (before0 + 1):
                after0 += 1
            elif pos < (before0 + 1):
                before0 += 1

        return after_num

if __name__ == "__main__":
    dec17_1().runtests()
    dec17_2().runtests()
