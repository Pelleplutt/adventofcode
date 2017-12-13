import task
import re

class dec13_1(task.str_task):
    def run_list(self, data):
        max = 0
        for d in data:
            m = re.match('(\d+): (\d+)', d)
            layer = int(m.group(1))
            depth = int(m.group(2))
            if layer > max:
                max = layer

        depths = []

        for i in range(max + 1):
            depths.append(0)

        for d in data:
            m = re.match('(\d+): (\d+)', d)
            layer = int(m.group(1))
            depth = int(m.group(2))
            depths[layer] = depth

        score = 0
        for i in range(max + 1):
            if depths[i] > 0 and (i % (depths[i] * 2 - 2)) == 0:
                score = score + depths[i] * i

        return score


class dec13_2(task.str_task):
    def run_list(self, data):
        max = 0
        for d in data:
            m = re.match('(\d+): (\d+)', d)
            layer = int(m.group(1))
            depth = int(m.group(2))
            if layer > max:
                max = layer

        depths = []

        for i in range(max + 1):
            depths.append(0)

        for d in data:
            m = re.match('(\d+): (\d+)', d)
            layer = int(m.group(1))
            depth = int(m.group(2))
            depths[layer] = depth

        delay = 0
        while True:
            score = 0

            for i in range(max + 1):
                n = i + delay
                if depths[i] > 0 and (n % (depths[i] * 2 - 2)) == 0:
                    score = 1
                    break

            if score == 0:
                return delay

            delay += 1

        return None

if __name__ == "__main__":
    dec13_1().runtests()
    dec13_2().runtests()
