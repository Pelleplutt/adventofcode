import task

class dec25_1(task.int_task):
    def run(self, line):

        state = 'A'
        pos = 0
        vals = [0]

        for i in range(line):
            currval = vals[pos]
            nv, mv, ns = (None, None, None)

            if state == 'A':
                if currval == 0:
                    nv = 1
                    mv = 1
                    ns = 'B'
                else:
                    nv = 0
                    mv = -1
                    ns = 'F'
            elif state == 'B':
                if currval == 0:
                    nv = 0
                    mv = 1
                    ns = 'C'
                else:
                    nv = 0
                    mv = 1
                    ns = 'D'
            elif state == 'C':
                if currval == 0:
                    nv = 1
                    mv = -1
                    ns = 'D'
                else:
                    nv = 1
                    mv = 1
                    ns = 'E'
            elif state == 'D':
                if currval == 0:
                    nv = 0
                    mv = -1
                    ns = 'E'
                else:
                    nv = 0
                    mv = -1
                    ns = 'D'
            elif state == 'E':
                if currval == 0:
                    nv = 0
                    mv = 1
                    ns = 'A'
                else:
                    nv = 1
                    mv = 1
                    ns = 'C'
            elif state == 'F':
                if currval == 0:
                    nv = 1
                    mv = -1
                    ns = 'A'
                else:
                    nv = 1
                    mv = 1
                    ns = 'A'
            vals[pos] = nv

            if mv == -1:
                if pos == 0:
                    vals.insert(0, 0)
                else:
                    pos -= 1
            else:
                pos += 1
                if pos == len(vals):
                    vals.append(0)

            state = ns

        return vals.count(1)


class dec25_2(task.int_task):
#class dec25_2(task.str_task):
    """
    """
    def run(self, line):
        pass

    def run_list(self, data):
        pass


if __name__ == "__main__":
    dec25_1().runtests()
    dec25_2().runtests()
