import task

class dec09_1(task.str_task):
    """
    """
    def parse_group(self, pos, line, score):
        localscore = score
        while pos < len(line):
            if line[pos] == '!':
                pos = pos + 1
            elif line[pos] == '{':
                pos, scoreadd = self.parse_group(pos + 1, line, score + 1)
                localscore = localscore + scoreadd
            elif line[pos] == '}':
                return pos, localscore
            elif line[pos] == '<':
                while pos < len(line):
                    if line[pos] == '!':
                        pos = pos + 1
                    elif line[pos] == '>':
                        break
                    pos = pos + 1

            pos = pos + 1
        return pos, localscore

    def run(self, line):
        pos, score =  self.parse_group(0, line, 0)
        return score

class dec09_2(task.str_task):
    """
    """
    def parse_group(self, pos, line):
        localscore = 0
        while pos < len(line):
            if line[pos] == '!':
                pos = pos + 1
            elif line[pos] == '{':
                pos, scoreadd = self.parse_group(pos + 1, line)
                localscore = localscore + scoreadd
            elif line[pos] == '}':
                return pos, localscore
            elif line[pos] == '<':
                pos = pos + 1
                while pos < len(line):
                    if line[pos] == '!':
                        pos = pos + 1
                    elif line[pos] == '>':
                        break
                    else:
                        localscore = localscore + 1
                    pos = pos + 1

            pos = pos + 1
        return pos, localscore

    def run(self, line):
        pos, score =  self.parse_group(0, line)
        return score


if __name__ == "__main__":
    dec09_1().runtests()
    dec09_2().runtests()
