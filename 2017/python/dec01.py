import task
import pprint

class dec01_1(task.task):
    def run(self, data):
        sum = 0
        if len(data) > 1:
            for idx, d in enumerate(data):
                if data[idx - 1] == d:
                    sum = sum + int(d)
        return str(sum)

class dec01_2(task.task):
    def run(self, data):
        sum = 0
        half = int(len(data) / 2)
        for idx, d in enumerate(data[:half]):
            if d == data[half + idx]:
                sum = sum + int(d) * 2
        return str(sum)

if __name__ == "__main__":
    dec01_1().main()
    dec01_2().main()
