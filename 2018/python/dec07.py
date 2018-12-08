import task

class dec07_1(task.str_task):
    def run_list(self, data):
        dep = {}
        objs = {}
        for line in data:
            obj = line[5]
            refobj = line[36]

            if dep.get(refobj) is None:
                dep[refobj] = {}
            dep[refobj][obj] = 1
            objs[refobj] = 1
            objs[obj] = 1

        order = ''
        while len(objs):
            candidates = []
            for o in objs:
                if o not in dep:
                    candidates.append(o)
            candidates.sort()

            c = candidates[0]
            order += c
            objs.pop(c)

            topop = []
            for refobj in dep.keys():
                dep[refobj].pop(c, 0)
                if not dep[refobj]:
                    topop.append(refobj)

            for refobj in topop:
                dep.pop(refobj, 0)

        return order

        

class dec07_2(task.str_task):
    def run_list(self, data):
        dep = {}
        objs = {}
        workercount = int(data[0])
        for line in data[1:]:
            obj = line[5]
            refobj = line[36]

            if dep.get(refobj) is None:
                dep[refobj] = {}
            dep[refobj][obj] = 1
            objs[refobj] = 1
            objs[obj] = 1

        doneorder = ''
        busyworkers = 0
        seconds = 0
        workers_busytime = []
        workers_task = []
        while len(objs):
            candidates = []
            for o in objs:
                if o not in dep and o not in workers_task:
                    candidates.append(o)
            candidates.sort()

            while candidates and busyworkers < workercount:
                c = candidates.pop(0)
                busyworkers += 1
                workers_busytime.append(60 + ord(c) - 64)
                workers_task.append(c)

            msleep = min(workers_busytime)
            seconds += msleep
            i = 0
            while i < len(workers_busytime):
                if workers_busytime[i] - msleep == 0:
                    workers_busytime.pop(i)
                    busyworkers -= 1
                    c = workers_task.pop(i)
                    objs.pop(c)
                    doneorder += c
                    
                    topop = []
                    for refobj in dep.keys():
                        dep[refobj].pop(c, 0)
                        if not dep[refobj]:
                            topop.append(refobj)

                    for refobj in topop:
                        dep.pop(refobj, 0)

                else:
                    workers_busytime[i] -= msleep
                    i += 1

        return seconds


if __name__ == "__main__":
    dec07_1().runtests()
    dec07_2().runtests()
