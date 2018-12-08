import task

class Dec01_1(task.IntTask):
    def run_list(self, data):
        s = 0
        for i in data:
            s += i
        return s

class Dec01_2(task.IntTask):
    def run_list(self, data):
        s = 0
        slist = [0]
        while True:
            for i in data:
                s += i
                if s in slist:
                    return s
                slist.append(s)

        return None


if __name__ == "__main__":
    dec01_1().runtests()
    dec01_2().runtests()
