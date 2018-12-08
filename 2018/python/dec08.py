import task

class dec08_1(task.str_task):
    def parse_node(self, pos, data):
        child_count = data[pos]
        metadata_count = data[pos + 1]
        metadata = []
        metadata_sum = 0
        pos += 2

        for i in range(child_count):
            pos, sub_metadata_sum = self.parse_node(pos, data)
            metadata_sum += sub_metadata_sum

        for md in range(metadata_count):
            metadata.append(data[pos])
            metadata_sum += data[pos]
            pos += 1

        return pos, metadata_sum

    def run(self, line):
        data = list(map(lambda x: int(x), line.split(' ')))
        pos, metadata_sum = self.parse_node(0, data)
        return metadata_sum


class dec08_2(task.str_task):
    def parse_node(self, pos, data):
        child_count = data[pos]
        children = []
        metadata_count = data[pos + 1]
        metadata = []
        metadata_sum = 0
        pos += 2

        for i in range(child_count):
            pos, sub_metadata_sum = self.parse_node(pos, data)
            children.append(sub_metadata_sum)
        for i in range(metadata_count):
            md = data[pos]
            pos += 1
            if child_count == 0:
                metadata.append(md)
                metadata_sum += md
            else:
                if md <= len(children):
                    metadata_sum += children[md - 1]

        return pos, metadata_sum

    def run(self, line):
        data = list(map(lambda x: int(x), line.split(' ')))
        pos, metadata_sum = self.parse_node(0, data)
        return metadata_sum

if __name__ == "__main__":
    dec08_1().runtests()
    dec08_2().runtests()
