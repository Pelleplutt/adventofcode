import task

class dec01_1(task.task):
    def run(self, data):
        sum = 0
        ld = data[-1]
        if len(data) > 1:
            for d in data:
                if ld == d:
                    sum = sum + int(d)
                ld = d
        return str(sum)

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        t = dec01_1()
        for a in sys.argv[1:]:
            print("{0}: {1}".format(a, t.run(a)))
        pass
    else:
        dec01_1().runtests()

