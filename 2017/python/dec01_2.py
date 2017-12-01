import task

class dec01_2(task.task):
    def run(self, data):
        sum = 0
        l = len(data)
        d0 = data[:int(l / 2)]
        d1 = data[int(l / 2):]
        for idx, d in enumerate(d0):
            if d == d1[idx]:
                sum = sum + int(d) * 2
        return str(sum)

if __name__ == "__main__":
    dec01_2().main()
