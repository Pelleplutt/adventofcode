import task

class dec06_1(task.str_task):
    def run(self, line):
        data = list(map(lambda x: int(x), line.split()))
        states = {}
        count = len(data)
        loops = 0

        state = ','.join(map(lambda x: str(x), data))
        states[state] = 1
        while True:
            max = None
            maxidx = None
            for idx, d in enumerate(data):
                if max is None or d > max:
                    maxidx = idx
                    max = d

            data[maxidx] = 0
            while max > 0:
                maxidx = (maxidx + 1) % count
                data[maxidx] = data[maxidx] + 1
                max = max - 1

            loops = loops + 1
            state = ','.join(map(lambda x: str(x), data))
            if states.get(state) is not None:
                return loops
            states[state] = 1

class dec06_2(task.str_task):
    def run(self, line):
        data = list(map(lambda x: int(x), line.split()))
        states = {}
        count = len(data)
        loops = 0

        state = ','.join(map(lambda x: str(x), data))
        states[state] = 0
        while True:
            max = None
            maxidx = None
            for idx, d in enumerate(data):
                if max is None or d > max:
                    maxidx = idx
                    max = d

            data[maxidx] = 0
            while max > 0:
                maxidx = (maxidx + 1) % count
                data[maxidx] = data[maxidx] + 1
                max = max - 1

            loops = loops + 1
            state = ','.join(map(lambda x: str(x), data))
            if states.get(state) is not None:
                return loops - states[state]
            states[state] = loops

if __name__ == "__main__":
    dec06_1().runtests()
    dec06_2().runtests()
