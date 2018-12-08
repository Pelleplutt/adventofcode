import task
import string

class Dec05_1(task.StrTask):
    def run(self, line):
        newline = ''
        linepos = 0
        linelength = len(line)

        while linepos < linelength:
            if newline == '':
                newline = line[linepos]
                linepos += 1
                continue

            c1 = line[linepos]
            c2 = newline[-1]

            if c1.isupper() != c2.isupper() and c1.upper() == c2.upper():
                newline = newline[:-1]
            else:
                newline += line[linepos]
            linepos += 1

        return len(newline)



class Dec05_2(task.StrTask):
    def calc_polymer(self, strip, line):
        line = line.replace(strip, '').replace(strip.upper(), '')

        newline = ''
        linepos = 0
        linelength = len(line)

        while linepos < linelength:
            if newline == '':
                newline = line[linepos]
                linepos += 1
                continue

            c1 = line[linepos]
            c2 = newline[-1]

            if c1.isupper() != c2.isupper() and c1.upper() == c2.upper():
                newline = newline[:-1]
            else:
                newline += line[linepos]
            linepos += 1

        return len(newline)

    def run(self, line):
        short = None
        for letter in string.ascii_lowercase:
            l = self.calc_polymer(letter, line)
            if short is None or short > l:
                short = l
        return short

if __name__ == "__main__":
    #dec05_1().runtests()
    dec05_2().runtests()
