import task

class dec04_1(task.str_task):
    def run_list(self, data):
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

        return valid

class dec04_2(task.str_task):
    def run_list(self, data):
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

        return valid

if __name__ == "__main__":
    dec04_1().runtests()
    dec04_2().runtests()
