import task

class Dec06_1(task.StrTask):

    def findclosest(self, x, y, points):
        min_dist = None
        min_dist_point = None
        for i in range(len(points)):
            px, py = points[i]

            dist = abs(x - px) + abs(y - py)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_dist_point = i

        for i in range(len(points)):
            px, py = points[i]

            dist = abs(x - px) + abs(y - py)
            if dist == min_dist and i != min_dist_point:
                return None

        return min_dist_point

    def run_list(self, data):
        xmax = 0
        ymax = 0

        points = []

        for l in data:
            x, y = map(lambda x: int(x), l.split(', '))

            if x > xmax:
                xmax = x
            if y > ymax:
                ymax = y

            points.append([x, y])

        counts = {}
        field = []
        for y in range(0, ymax + 1):
            line = []
            for x in range(xmax + 1):
                closest = self.findclosest(x, y, points)
                counts[closest] = counts.get(closest, 0) + 1
                line.append(closest)
            field.append(line)

        for closest in field[0]:
            if closest is not None:
                counts.pop(closest, 0)

        for closest in field[-1]:
            if closest is not None:
                counts.pop(closest, 0)

        for line in field:
            if line[0] is not None:
                counts.pop(line[0], 0)
            if line[-1] is not None:
                counts.pop(line[-1], 0)

        return max(counts.values())
        

class Dec06_2(task.StrTask):
    def totaldistance(self, x, y, points):
        dist = 0
        for i in range(len(points)):
            px, py = points[i]

            dist += abs(x - px) + abs(y - py)

        return dist

    def run_list(self, data):
        xmax = 0
        ymax = 0

        points = []
        maxdist = int(data[0])
        for l in data[1:]:
            x, y = map(lambda x: int(x), l.split(', '))

            if x > xmax:
                xmax = x
            if y > ymax:
                ymax = y

            points.append([x, y])

        count = 0
        for y in range(ymax + 1):
            for x in range(xmax + 1):
                dist = self.totaldistance(x, y, points)
                if dist < maxdist:
                    count += 1
        
        return count


if __name__ == "__main__":
    dec06_1().runtests()
    dec06_2().runtests()
