import task

class dec21_1(task.str_task):
    def sq_flip_horizontal(self, sq):
        if len(sq) == 3:
            return [sq[0][::-1], sq[1][::-1], sq[2][::-1]]
        else:
            return [sq[0][::-1], sq[1][::-1]]

    def sq_rotate(self, sq):
        if len(sq) == 3:
            return [sq[2][0] + sq[1][0] + sq[0][0],
                    sq[2][1] + sq[1][1] + sq[0][1],
                    sq[2][2] + sq[1][2] + sq[0][2]]
        else:
            return [sq[1][0] + sq[0][0],
                    sq[1][1] + sq[0][1]]

    def sq_split(self, img, divisor):
        splits = int(len(img) / divisor)
        if splits == 1:
            yield img.copy()
        else:
            for y in range(splits):
                for x in range(splits):
                    xpos = x * divisor
                    ypos = y * divisor

                    ret = []
                    for row in range(divisor):
                        ret.append(img[ypos + row][xpos:xpos + divisor])
                    yield(ret)

    def run_list(self, data):
        iterations = int(data[0])
        img = ['.#.', '..#', '###']

        rules = {}

        for rule in data[1:]:
            rin, rout = rule.split(' => ')
            rules[rin] = rout.split('/')

        for iter in range(iterations):
            divisor = None
            if len(img) % 2 == 0:
                divisor = 2
            elif len(img) % 3 == 0:
                divisor = 3

            matches = []
            for sq in self.sq_split(img, divisor):
                v1 = sq
                for rot in range(4):
                    v1 = self.sq_rotate(v1)
                    v2 = self.sq_flip_horizontal(v1)

                    v1s = '/'.join(v1)
                    v2s = '/'.join(v2)

                    if rules.get(v1s) is not None:
                        matches.append(rules[v1s])
                        break
                    elif rules.get(v2s) is not None:
                        matches.append(rules[v2s])
                        break

            splits = int(len(img) / divisor)
            if splits == 1:
                img = matches[0]
            else:
                img = []
                newsize = len(matches[0])
                for split in range(splits):
                    for newline in range(newsize):
                        line = ''
                        for col in range(splits):
                            line += matches[split * splits + col][newline]
                        img.append(line)

        count = 0
        for line in img:
            count += line.count('#')

        return count


class dec21_2(dec21_1):
    pass

if __name__ == "__main__":
    dec21_1().runtests()
    dec21_2().runtests()
