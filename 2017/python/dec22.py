import task

class dec22_1(task.str_task):
    def run_list(self, data):
        xpos = int(len(data[0]) / 2)
        ypos = int(len(data) / 2)
        dir = 0
        count = 0

        for i in range(10000):
            if data[ypos][xpos] == '.':
                dir -= 1
                if dir == -1:
                    dir = 3
                data[ypos] = data[ypos][:xpos] + '#' + data[ypos][xpos + 1:]
                count += 1
            else:
                dir = (dir + 1) % 4
                data[ypos] = data[ypos][:xpos] + '.' + data[ypos][xpos + 1:]

            if dir == 0:
                if ypos == 0:
                    data.insert(0, '.' * len(data[0]))
                else:
                    ypos -= 1
            elif dir == 1:
                if xpos + 1 == len(data[0]):
                    for idx in range(len(data)):
                        data[idx] += '.'
                xpos += 1
            elif dir == 2:
                if ypos + 1 == len(data):
                    data.append('.' * len(data[0]))
                ypos += 1
            elif dir == 3:
                if xpos == 0:
                    for idx in range(len(data)):
                        data[idx] = '.' + data[idx]
                else:
                    xpos -= 1
        return count

class dec22_2(task.str_task):
    def run_list(self, data):
        xpos = int(len(data[0]) / 2)
        ypos = int(len(data) / 2)
        dir = 0
        count = 0

        for i in range(10000000):
            if data[ypos][xpos] == '.':
                dir -= 1
                if dir == -1:
                    dir = 3
                data[ypos] = data[ypos][:xpos] + 'W' + data[ypos][xpos + 1:]
            elif data[ypos][xpos] == '#':
                dir = (dir + 1) % 4
                data[ypos] = data[ypos][:xpos] + 'F' + data[ypos][xpos + 1:]
            elif data[ypos][xpos] == 'W':
                data[ypos] = data[ypos][:xpos] + '#' + data[ypos][xpos + 1:]
                count += 1
            elif data[ypos][xpos] == 'F':
                dir = (dir + 2) % 4
                data[ypos] = data[ypos][:xpos] + '.' + data[ypos][xpos + 1:]

            if dir == 0:
                if ypos == 0:
                    data.insert(0, '.' * len(data[0]))
                else:
                    ypos -= 1
            elif dir == 1:
                if xpos + 1 == len(data[0]):
                    for idx in range(len(data)):
                        data[idx] += '.'
                xpos += 1
            elif dir == 2:
                if ypos + 1 == len(data):
                    data.append('.' * len(data[0]))
                ypos += 1
            elif dir == 3:
                if xpos == 0:
                    for idx in range(len(data)):
                        data[idx] = '.' + data[idx]
                else:
                    xpos -= 1

        return count


if __name__ == "__main__":
    dec22_1().runtests()
    dec22_2().runtests()
