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
    dec01_1().main()
