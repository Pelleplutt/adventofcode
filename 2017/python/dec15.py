import task

class dec15_1(task.int_task):
    def run_list(self, data):
        d1 = data[0]
        d2 = data[1]

        count = 0
        for i in range(40000000):
            d1 = (d1 * 16807) % 2147483647
            d2 = (d2 * 48271) % 2147483647

            if d1 & 0xffff == d2 & 0xffff:
                count += 1

        return count

class dec15_2(task.int_task):
    def run_list(self, data):
        d1 = data[0]
        d2 = data[1]

        count = 0
        for i in range(5000000):
            while True:
                d1 = (d1 * 16807) % 2147483647
                if d1 % 4 == 0:
                    break
            while True:
                d2 = (d2 * 48271) % 2147483647
                if d2 % 8 == 0:
                    break

            if d1 & 0xffff == d2 & 0xffff:
                count += 1

        return count

if __name__ == "__main__":
    dec15_1().runtests()
    dec15_2().runtests()
