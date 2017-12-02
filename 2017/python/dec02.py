import task

class dec02_1(task.task):
    def init(self):
        self.in_multiline = True

    def rowchecksum(self, row):
        minv = min(row)
        maxv = max(row)
        return maxv - minv

    def run(self, data):
        sum = 0
        for line in data:
            sum = sum + self.rowchecksum(list(map(lambda x: int(x), line.split())))
        return str(sum)

class dec02_2(task.task):
    def init(self):
        self.in_multiline = True

    def rowchecksum(self, row):
        row = sorted(row)
        for numerator in reversed(row):
            for denumerator in row:
                if denumerator < numerator:
                    if numerator % denumerator == 0:
                        return int(numerator/denumerator)
                else:
                    break
        return 0

    def run(self, data):
        sum = 0
        for line in data:
            sum = sum + self.rowchecksum(list(map(lambda x: int(x), line.split())))
        return str(sum)

if __name__ == "__main__":
    dec02_1().main()
    dec02_2().main()
