import task
import re

class dec13_1(task.str_task):
    def run_list(self, data):
        max = 0
        for d in data:
            m = re.match('(\d+): (\d+)', d)
            layer = int(m.group(1))
            depth = int(m.group(2))
            if layer > max:
                max = layer

        depths = []
        layers = []
        dirs = []

        for i in range(max + 1):
            depths.append(0)
            layers.append(0)
            dirs.append(1)

        for d in data:
            m = re.match('(\d+): (\d+)', d)
            layer = int(m.group(1))
            depth = int(m.group(2))
            depths[layer] = depth
            layers[layer] = 0

        score = 0
        for i in range(max + 1):
            if depths[i] > 0 and layers[i] == 0:
                score = score + depths[i] * i
            for l in range(max + 1):
                if depths[l] > 0:
                    if layers[l] == 0 and dirs[l] == -1:
                        dirs[l] = 1
                    if layers[l] == depths[l] - 1 and dirs[l] == 1:
                        dirs[l] = -1

                    layers[l] = layers[l] + dirs[l]

        return score




class dec13_2(task.str_task):
    def run_list(self, data):
        max = 0
        for d in data:
            m = re.match('(\d+): (\d+)', d)
            layer = int(m.group(1))
            depth = int(m.group(2))
            if layer > max:
                max = layer
        depths = []

        for i in range(max + 1):
            depths.append(0)

        for d in data:
            m = re.match('(\d+): (\d+)', d)
            layer = int(m.group(1))
            depth = int(m.group(2))
            depths[layer] = depth

        initiallayers = []
        initialdirs = []
        for i in range(max + 1):
            initiallayers.append(0)
            initialdirs.append(1)

        for delay in range(200000000):
            score = 0
            layers = initiallayers.copy()
            dirs = initialdirs.copy()

            for i in range(max + 1):
                if depths[i] > 0 and layers[i] == 0:
                    score = 1
                    break
                for l in range(max + 1):
                    if depths[l] > 0:
                        if layers[l] == 0 and dirs[l] == -1:
                            dirs[l] = 1
                        if layers[l] == depths[l] - 1 and dirs[l] == 1:
                            dirs[l] = -1

                        layers[l] = layers[l] + dirs[l]
            if score == 0:
                return delay

            for l in range(max + 1):
                if depths[l] > 0:
                    if initiallayers[l] == 0 and initialdirs[l] == -1:
                        initialdirs[l] = 1
                    if initiallayers[l] == depths[l] - 1 and initialdirs[l] == 1:
                        initialdirs[l] = -1

                    initiallayers[l] = initiallayers[l] + initialdirs[l]

        return None


if __name__ == "__main__":
    dec13_1().runtests()
    dec13_2().runtests()
