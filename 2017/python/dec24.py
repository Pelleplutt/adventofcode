import task
import collections

class dec24_1(task.str_task):
    def build(self, ports, bridge, usedports, starttype):
        bestbridge = bridge
        bestbridgestrength = self.strength(bridge)
        for outp in ports[starttype]:
            # requires that each component is unique, but this seems to be the case
            if starttype > outp:
                descstr = str(starttype) + '/' + str(outp)
            else:
                descstr = str(outp) + '/' + str(starttype)
            if usedports.get(descstr) is not None:
                continue
            newbridge, newstrength = self.build(ports, [*bridge, (starttype, outp)], {**usedports, descstr: 1}, outp)
            if newbridge is not None and (bestbridgestrength is None or newstrength > bestbridgestrength):
                bestbridge = newbridge
                bestbridgestrength = newstrength
        return bestbridge, bestbridgestrength

    def strength(self, bridge):
        s = 0
        for p in bridge:
            inp, outp = p
            s += inp + outp

        return s

    def run_list(self, data):
        ports = collections.defaultdict(list)
        for p in data:
            inp, outp = [int(x) for x in p.split('/')]
            ports[inp].append(outp)
            ports[outp].append(inp)

        bestbridge, bs = self.build(ports, [], {}, 0)

        return bs


class dec24_2(task.str_task):
    def build(self, ports, bridge, usedports, starttype):
        bestbridge = bridge
        bestbridgestrength = self.strength(bridge)
        bestbridgelength = len(bridge)
        for outp in ports[starttype]:
            # requires that each component is unique, but this seems to be the case
            if starttype > outp:
                descstr = str(starttype) + '/' + str(outp)
            else:
                descstr = str(outp) + '/' + str(starttype)
            if usedports.get(descstr) is not None:
                continue
            newbridge, newstrength, newlength = self.build(ports, [*bridge, (starttype, outp)], {**usedports, descstr: 1}, outp)

            if newbridge is not None and (bestbridgelength is None or (newlength > bestbridgelength) or (newlength == bestbridgelength and newstrength > bestbridgestrength)):
                bestbridge = newbridge
                bestbridgestrength = newstrength
                bestbridgelength = newlength
        return bestbridge, bestbridgestrength, bestbridgelength

    def strength(self, bridge):
        s = 0
        for p in bridge:
            inp, outp = p
            s += inp + outp

        return s

    def run_list(self, data):
        ports = collections.defaultdict(list)
        for p in data:
            inp, outp = [int(x) for x in p.split('/')]
            ports[inp].append(outp)
            ports[outp].append(inp)

        bestbridge, bs, bl = self.build(ports, [], {}, 0)

        return bs

if __name__ == "__main__":
    dec24_1().runtests()
    dec24_2().runtests()
