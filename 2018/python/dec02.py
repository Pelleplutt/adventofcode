import task

class dec02_1(task.str_task):
    def run_list(self, data):
        twos = 0
        threes = 0
        for s in data:
            counts = {}
            for c in s:
                counts[c] = counts.get(c, 0) + 1

            if 3 in counts.values():
                threes += 1
            if 2 in counts.values():
                twos += 1

        return twos * threes



class dec02_2(task.str_task):
    def find1diff(self, s1, s2):
        d = 0
        dp = -1
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                d += 1
                dp = i
                if d > 1:
                    return None

        if d < 1:
            return None
        print("1 diff: {0}: {1}=={2}, dp={3}".format(d, s1, s2, dp))
        if dp == 0:
            return s1[1:]
        return s1[:dp] + s1[dp + 1:]


    def run_list(self, data):
        
        for i in range(0, len(data)):
            s1 = data[i]
            for j in range(i + 1, len(data)):
                s2 = data[j]

                common = self.find1diff(s1, s2)
                if common is not None:
                    return common

        return None
        


if __name__ == "__main__":
    dec02_1().runtests()
    dec02_2().runtests()
