import task
import re
import collections

class dec12_1(task.str_task):
    def findzero(self, peers, id, visited):
        if id in visited:
            return 0
        visited.add(id)
        for peer in peers[id]:
            self.findzero(peers, peer, visited)

    def run_list(self, data):
        comm = collections.defaultdict(list)
        for line in data:
            m = re.match('^(\d+) <-> (.*)', line)
            id = int(m.group(1))
            peers = m.group(2).split(', ')

            for p in peers:
                p = int(p)
                comm[id].append(p)
                comm[p].append(id)

        visited = set()
        self.findzero(comm, 0, visited)

        return len(visited)

class dec12_2(task.str_task):
    def findzero(self, peers, startid, id, visited):
        if id in visited:
            return 0
        visited.add(id)

        for peer in peers[id]:
            self.findzero(peers, startid, peer, visited)

    def run_list(self, data):
        comm = collections.defaultdict(list)
        for line in data:
            m = re.match('^(\d+) <-> (.*)', line)
            id = int(m.group(1))
            peers = m.group(2).split(', ')

            for p in peers:
                p = int(p)
                comm[id].append(p)
                comm[p].append(id)

        groups = {}
        for id in comm:
            visited = set()
            self.findzero(comm, id, id, visited)
            keylist = list(sorted(visited))
            key = ','.join(map(lambda x: str(x), keylist))
            groups[key] = 1

        return len(groups)

if __name__ == "__main__":
    dec12_1().runtests()
    dec12_2().runtests()
