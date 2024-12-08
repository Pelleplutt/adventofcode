#!/usr/bin/env python3

import pprint
import re
import sys
import task

class Dec08(task.Task):
    def find_nodes(self, data, node):
        # find all occurencies of node, return tuples of x, y for the positions
        ll = len(data[0])
        return list(map(lambda p: (p % ll, int(p / ll)), [i for i, ltr in enumerate(''.join(data)) if ltr == node]))
        

class Dec08a(Dec08):
    def run(self, data):
        antennas = set(''.join(data))
        antennas.discard('.')
        antennas.discard('#')

        width = len(data[0])
        height = len(data)

        antinodes = set()

        for antenna in antennas:
            nodes = self.find_nodes(data, antenna)
            if len(nodes) >= 2:
                for i1, n1 in enumerate(nodes):
                    for n2 in nodes[i1 + 1:]:
                        dx = n1[0] - n2[0]
                        dy = n1[1] - n2[1]

                        nx = n1[0] + dx
                        ny = n1[1] + dy
                        if nx >= 0 and ny >= 0 and nx < width and ny < height:
                            antinodes.add(f"{nx},{ny}")
                        nx = n2[0] - dx
                        ny = n2[1] - dy
                        if nx >= 0 and ny >= 0 and nx < width and ny < height:
                            antinodes.add(f"{nx},{ny}")
        return len(antinodes)





class Dec08b(Dec08):
    def run(self, data):
        antennas = set(''.join(data))
        antennas.discard('.')
        antennas.discard('#')

        width = len(data[0])
        height = len(data)

        antinodes = set()

        for antenna in antennas:
            nodes = self.find_nodes(data, antenna)
            if len(nodes) >= 2:
                for i1, n1 in enumerate(nodes):
                    for n2 in nodes[i1 + 1:]:
                        dx = n1[0] - n2[0]
                        dy = n1[1] - n2[1]

                        nx, ny = n1[0], n1[1]
                        while nx >= 0 and ny >= 0 and nx < width and ny < height:
                            antinodes.add(f"{nx},{ny}")
                            nx = nx + dx
                            ny = ny + dy

                        nx, ny = n2[0], n2[1]
                        while nx >= 0 and ny >= 0 and nx < width and ny < height:
                            antinodes.add(f"{nx},{ny}")
                            nx = nx - dx
                            ny = ny - dy

                        
        return len(antinodes)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec08a().run_specific_tests(sys.argv[1:])
        Dec08b().run_specific_tests(sys.argv[1:])
    else:
        Dec08a().runtests()
        Dec08b().runtests()
