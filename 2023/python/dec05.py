#!/usr/bin/env python3

import pprint
import sys
import task

class Dec05a(task.StrTask):
#class Dec05a(task.IntTask):
    """
    """
    def get_map_value(self, data, value):
        last_m = None
        for m in data:
            if value < m[1]:
                return value
            elif value < m[1] + m[2]:
                return m[0] + (value - m[1])
        return value
                    
    def run_list(self, data):
        seeds = data[0]
        seeds = map(lambda x: int(x), seeds[seeds.index(':') + 2:].split())

        map_name = None
        map_data = None
        maps = {}
        for d in data[2:]:
            if len(d):
                if map_name is not None:
                    map_data += [list(map(lambda x: int(x), d.split()))]
                else:
                    map_name = d.split()[0]
                    map_data = []
            elif map_name:
                maps[map_name] = map_data
                map_name = None
                map_data = None

        if map_name is not None:
            maps[map_name] = map_data

        for k, v in maps.items():
            maps[k] = sorted(v, key=lambda x: x[1])

        locations = []
        for s in seeds:
            map_path = [
                'seed-to-soil',
                'soil-to-fertilizer',
                'fertilizer-to-water',
                'water-to-light',
                'light-to-temperature',
                'temperature-to-humidity',
                'humidity-to-location'
            ]
            v = s
            for p in map_path:
                #bv = v
                v = self.get_map_value(maps[p], v)
                #print(f"{s:3}: {p}({bv}) -> {v}")
            locations += [v]

        return sorted(locations)[0]


class Dec05b(task.StrTask):
    """
    """
    def get_map_value(self, data, value):
        for m in data:
            if value < m[1]:
                return value
            elif value < m[1] + m[2]:
                return m[0] + (value - m[1])
        return value
    
    def get_map_edge_cases_in_interval(self, data, min, max):
        last_m = None
        # List of (from, to) pair of intervals in the interval
        edge_cases = []

        #'seed-to-soil': [[52, 50, 48], [50, 98, 2]],
        #79 93
        #55 68

        in_interval = False
        interval_start = None
        for i in range(len(data)):
            m = data[i]
            
            print(f"testing min {min} and max {max} within {m[1]} - {m[1] + m[2]}")
            if in_interval:
                if max < m[1] + m[2]:
                    print(f" in interval: adding interval to max {interval_start} - {max}")
                    edge_cases += [[interval_start, max]]
                    in_interval = False
                    break
                else:
                    print(f" in interval: adding full interval {interval_start} - {m[1] + m[2]}")
                    edge_cases += [[interval_start, m[1] + m[2]]]
                    interval_start = m[1] + m[2]
            elif min <= m[1] and max >= m[1]:
                edge_cases += [[min, max]]
                if max < m[1] + m[2]:
                    print(f" out interval: adding min to max {min} - {max}")
                    edge_cases += [[min, max]]
                    break
                else:
                    in_interval = True
                    interval_start = min
                    print(f" out interval: setting start of interval at {min}")
                    #print(f" out interval: adding min to start of interval {min} - {m[1]}")
                    #edge_cases += [[min, m[1]]]
                    #in_interval = True
            elif min >= m[1] and min < m[1] + m[2]:
                if max < m[1] + m[2]:
                    print(f" out interval: adding min to max {min} - {max}")
                    edge_cases += [[min, max]]
                    break
                else:
                    in_interval = True
                    interval_start = min
                    print(f" out interval: setting start of interval at {min}")
                    #print(f" out interval: adding min to start of interval {min} - {m[1]}")
                    #edge_cases += [[min, m[1]]]
                    #in_interval = True


        if in_interval:
            edge_cases += [[data[-1][1], data[-1][1] + data[-1][2]]]

        if len(edge_cases) == 0:
            print(f" adding default {min} - {max}")
            edge_cases = [[min, max]]
            # return the full list of mapped values
        pprint.pprint(edge_cases)
        return list(map(lambda x: [self.get_map_value(data, x[0]), self.get_map_value(data, x[1])], edge_cases))
                    
    def run_list(self, data):
        seeds = data[0]
        seeds = list(map(lambda x: int(x), seeds[seeds.index(':') + 2:].split()))

        map_name = None
        map_data = None
        maps = {}
        for d in data[2:]:
            if len(d):
                if map_name is not None:
                    map_data += [list(map(lambda x: int(x), d.split()))]
                else:
                    map_name = d.split()[0]
                    map_data = []
            elif map_name:
                maps[map_name] = map_data
                map_name = None
                map_data = None

        if map_name is not None:
            maps[map_name] = map_data

        for k, v in maps.items():
            maps[k] = sorted(v, key=lambda x: x[1])

        pprint.pprint(maps)
        locations = []
        for initial, count in zip(seeds[::2], seeds[1::2]):
            map_path = [
                'seed-to-soil',
                'soil-to-fertilizer',
                'fertilizer-to-water',
                'water-to-light',
                'light-to-temperature',
                'temperature-to-humidity',
                'humidity-to-location'
            ]
            edge_values = [[initial, initial + count]]
            for p in map_path:
                new_edge_values = []
                for e in edge_values:
                    print(p)
                    pprint.pprint(edge_values)
                    new_edge_values += self.get_map_edge_cases_in_interval(maps[p], e[0], e[1])
                    pprint.pprint(new_edge_values)
                edge_values = new_edge_values
            locations += edge_values

        return sorted(locations)[0]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec05a().run_tests_from_commandline()
        Dec05b().run_tests_from_commandline()
    else:
        Dec05a().runtests()
        Dec05b().runtests()
