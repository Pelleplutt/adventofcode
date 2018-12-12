import task

class dec12_1(task.StrTask):
    def run_list(self, data):
        pots = data[0]
        pmin = 0
        legend = {}
        for l in data[1:]:
            legend[l[:5]] = l[9]

        for generation in range(20):
            plen = len(pots)
            #     0
            #     #..#.#..##......###...###
            # ....#
            newpots = ''
            for i in range(-2, plen + 3):
                if i < 2:
                    m = '.' * (2 - i) + pots[0:(i + 3)]
                elif i > plen - 3:
                    m = pots[(i - 2):plen] + '.' * (i - plen + 3) 
                else:
                    m = pots[(i - 2):(i - 2 + 5)]

                newpots += legend.get(m, '.')

            first = 0
            for i in range(plen):
                if newpots[i] == '#':
                    first = i
                    break
            
            pots = newpots[first:].rstrip('.')
            pmin = pmin + first - 2

        score = 0
        for i in range(len(pots)):
            if pots[i] == '#':
                score += pmin + i
        return score

class dec12_2(task.StrTask):
    def run_list(self, data):
        pots = data[0]
        pmin = 0
        legend = {}
        for l in data[1:]:
            legend[l[:5]] = l[9]

        for generation in range(50000000000):
            plen = len(pots)
            newpots = ''
            for i in range(-2, plen + 3):
                if i < 2:
                    m = '.' * (2 - i) + pots[0:(i + 3)]
                elif i > plen - 3:
                    m = pots[(i - 2):plen] + '.' * (i - plen + 3) 
                else:
                    m = pots[(i - 2):(i - 2 + 5)]

                newpots += legend.get(m, '.')

            first = 0
            for i in range(plen):
                if newpots[i] == '#':
                    first = i
                    break
            
            strippedpots = newpots[first:].rstrip('.')

            if strippedpots == pots:
                pminbase = pmin
                pmindiff = first - 2
                npmin = pminbase + (50000000000 - generation) * pmindiff
                score = 0
                for i in range(len(pots)):
                    if pots[i] == '#':
                        score += npmin + i
                return score

            pots = strippedpots
            pmin = pmin + first - 2

        return None


if __name__ == "__main__":
    dec12_1().runtests()
    dec12_2().runtests()