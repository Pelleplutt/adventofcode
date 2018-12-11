import task

class dec11_1(task.IntTask):

    def get_cell_power(self, x, y):
        return self.grid[y - 1][x - 1]

    def calc_cell_power(self, x, y):
        rackid = x + 10
        power = (int((rackid * y + self.serial) * rackid / 100) % 10) - 5

        return power

    def set_grid(self):
        self.grid = []
        for y in range(300):
            row = []
            for x in range(300):
                row.append(self.calc_cell_power(x + 1, y + 1))
            self.grid.append(row)

    def max_square_from_grid(self, squaresize):
        maxpower = None
        maxpowerx = None
        maxpowery = None

        for y in range(1, 300 - squaresize + 1):
            xsums = []
            for x in range(1, 300):
                xsum = 0
                for y1 in range(squaresize):
                    xsum += self.get_cell_power(x, y + y1)
                xsums.append(xsum)

            for x in range(1, 300 - squaresize + 1):
                power = 0
                for x1 in range(squaresize):
                    power += xsums[x - 1 + x1]

                if maxpower is None or power > maxpower:
                    maxpower = power
                    maxpowerx = x
                    maxpowery = y

        return maxpower, maxpowerx, maxpowery

    def run(self, line):
        self.serial = line
        self.set_grid()
        maxpower, maxpowerx, maxpowery = self.max_square_from_grid(3)
        return '{},{}'.format(maxpowerx, maxpowery)



class dec11_2(task.IntTask):
    def find_max_size_at_pos(self, x, y):
        maxpower = None
        maxpowersize = None

        power = 0
        for size in range(1, 300 - max(x, y) - 1):
            if x + size > 300 or y + size > 300:
                return maxpower, maxpowersize

            if size == 1:
                power = self.d111.grid[y - 1][x - 1]
            else:
                for x1 in range(x, x + size):
                    power += self.d111.grid[y + size - 2][x1 - 1]
                for y1 in range(y, y + size - 1):
                    power += self.d111.grid[y1 - 1][x + size - 2]

            if maxpower is None or power > maxpower:
                maxpowersize = size
                maxpower = power
        
        return maxpower, maxpowersize

    def run(self, line):
        self.d111 = dec11_1()
        self.d111.serial = line
        self.d111.set_grid()

        maxpowersize = None
        maxpower = None
        maxpowerx = None
        maxpowery = None

        for y in range(1, 300):
            for x in range(1, 300):
                power, size = self.find_max_size_at_pos(x, y)
                if power is not None and (maxpower is None or power > maxpower):
                    maxpowersize = size
                    maxpower = power
                    maxpowerx = x
                    maxpowery = y

        return '{},{},{}'.format(maxpowerx, maxpowery, maxpowersize)


if __name__ == "__main__":
    dec11_1().runtests()
    dec11_2().runtests()
