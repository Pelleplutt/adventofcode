import task
import re

class dec07_1(task.str_task):
    """
    """
    def run_list(self, data):
        discs = {}
        for line in data:
            m = re.match('(.*) \((\d+)\) -> (.*)', line)
            if m is None:
                m = re.match('(.*) \((\d+)\)', line)
                id, weight = m.group(1,2)
                others = []
            else:
                id, weight, others = m.group(1,2,3)
                others = others.split(', ')

            discs[id] = {
                'weight': weight,
                'others': others
            }

        for did, disc in discs.items():
            for odid in disc['others']:
                discs[odid]['refs'] = 1

        for did, disc in discs.items():
            if disc.get('refs') is None:
                return did

        return None

class dec07_2(task.str_task):
    """
    """

    def stackweight(self, discs, id):
        disc = discs[id]
        if disc.get('stackweight') is None:
            w = disc['weight']
            for oid in discs[id]['others']:
                w = w + self.stackweight(discs, oid)
            disc['stackweight'] = w

        return disc['stackweight']

    def getoffendingchild(self, discs, disc):
        weights = {}
        maxw = None
        minw = None

        for oid, odisc in disc['others'].items():
            w = self.stackweight(discs, oid)
            weights[oid] = w
            if maxw is None or w > maxw:
                maxw = w
            if minw is None or w < maxw:
                minw = w

        if maxw is not None:
            if len(list(filter(lambda x: x != minw, weights.values()))) > 0:
                for oid, ow in weights.items():
                    if ow != minw:
                        return oid, maxw, minw

        return None, maxw, minw


    def getchildweightfix(self, discs, disc):
        offchild,  childminw, childmaxw = self.getoffendingchild(discs, disc)
        if offchild:
            roffchild, rchildsw, rchildgw = self.getoffendingchild(discs, discs[offchild])
            if roffchild is None:
                wdiff = childminw - childmaxw
                return discs[offchild]['weight'] - wdiff
            else:
                return self.getchildweightfix(discs, discs[offchild])

        return None

    def run_list(self, data):
        discs = {}
        for line in data:
            m = re.match('(.*) \((\d+)\) -> (.*)', line)
            others = {}
            if m is None:
                m = re.match('(.*) \((\d+)\)', line)
                id, weight = m.group(1,2)
            else:
                id, weight, ol = m.group(1,2,3)
                for oid in ol.split(', '):
                    others[oid] = -1

            discs[id] = {
                'id': id,
                'weight': int(weight),
                'others': others
            }

        for disc in discs.values():
            for odid in disc['others']:
                discs[odid]['refs'] = 1

        base = None
        for did, disc in discs.items():
            if disc.get('refs') is None:
                base = did
                break

        w = self.getchildweightfix(discs, discs[base])
        return w

if __name__ == "__main__":
    dec07_1().runtests()
    dec07_2().runtests()
