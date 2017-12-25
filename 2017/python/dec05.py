import task

class dec05_1(task.int_task):
    def run_list(self, data):
        max = len(data)
        count = 0
        ip = 0

        while ip < max and ip >= 0:
            next = data[ip]
            data[ip] = data[ip] + 1
            ip = ip + next
            count = count + 1

        return count

class dec05_2(task.int_task):
    def run_list(self, data):
        ip = 0
        max = len(data)
        count = 0

        while ip < max and ip >= 0:
            next = data[ip]
            if next >= 3:
                data[ip] = data[ip] - 1
            else:
                data[ip] = data[ip] + 1
            ip = ip + next
            count = count + 1

        return count

if __name__ == "__main__":
    dec05_1().runtests()
    dec05_2().runtests()
