import task

class dec11_1(task.str_task):
    def run(self, data):
        x, y, z = (0, 0, 0)
        for d in data.split(','):
            if d == 's':
                z = z + 1
                y = y - 1
            elif d == 'n':
                z = z - 1
                y = y + 1
            elif d == 'se':
                x = x + 1
                y = y - 1
            elif d == 'sw':
                z = z + 1
                x = x - 1
            elif d == 'ne':
                z = z - 1
                x = x + 1
            elif d == 'nw':
                x = x - 1
                y = y + 1

        steps = max(abs(x), abs(y), abs(z))

        return steps

class dec11_2(task.str_task):
    def run(self, data):
        x, y, z = (0, 0, 0)
        maxsteps = None
        for d in data.split(','):
            if d == 's':
                z = z + 1
                y = y - 1
            elif d == 'n':
                z = z - 1
                y = y + 1
            elif d == 'se':
                x = x + 1
                y = y - 1
            elif d == 'sw':
                z = z + 1
                x = x - 1
            elif d == 'ne':
                z = z - 1
                x = x + 1
            elif d == 'nw':
                x = x - 1
                y = y + 1

            steps = max(abs(x), abs(y), abs(z))
            if maxsteps is None or steps > maxsteps:
                maxsteps = steps

        return maxsteps

if __name__ == "__main__":
    dec11_1().runtests()
    dec11_2().runtests()
