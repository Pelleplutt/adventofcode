import task

class dec02_1(task.str_task):
    def rowchecksum(self, row):
        minv = min(row)
        maxv = max(row)
        return maxv - minv

    def run_list(self, data):
        sum = 0
        for line in data:
            sum = sum + self.rowchecksum(list(map(lambda x: int(x), line.split())))
        return sum

class dec02_2(task.str_task):
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

    def run_list(self, data):
        sum = 0
        for line in data:
            sum = sum + self.rowchecksum(list(map(lambda x: int(x), line.split())))
        return sum

if __name__ == "__main__":
    dec02_1().runtests()
    dec02_2().runtests()
