import task

class dec04_1(task.task):
    def init(self):
        self.in_multiline = True

    def run(self, data):
        valid = 0
        for line in data:
            dupe = {}
            linevalid = True
            for word in line.split():
                if dupe.get(word) is not None:
                    linevalid = False
                    break
                dupe[word] = 1
            if linevalid:
                valid = valid + 1

        return str(valid)

class dec04_2(task.task):
    def init(self):
        self.in_multiline = True

    def run(self, data):
        valid = 0
        for line in data:
            dupe = {}
            linevalid = True
            for word in line.split():
                word = ''.join(sorted(word))
                if dupe.get(word) is not None:
                    linevalid = False
                    break
                dupe[word] = 1
            if linevalid:
                valid = valid + 1

        return str(valid)

if __name__ == "__main__":
    dec04_1().main()
    dec04_2().main()
