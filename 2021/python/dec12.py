#!/usr/bin/env python3

import sys
import task

class Dec12a(task.StrTask):
    """
    """
    def navigate(self, cavesystem, completedpaths, visitedcaves, currentcave):
        for targetcave in cavesystem[currentcave]:
            if targetcave.islower() and targetcave in visitedcaves:
                pass
            elif targetcave == 'end':
                completedpaths.append(','.join([*visitedcaves, targetcave]))
            else:
                self.navigate(cavesystem, completedpaths, [*visitedcaves, targetcave], targetcave)

    def run_list(self, data):
        cavesystem = {}
        for path in data:
            cave1, cave2 = path.split('-')
            cavesystem.setdefault(cave1, []).append(cave2)
            cavesystem.setdefault(cave2, []).append(cave1)

        completedpaths = []
        self.navigate(cavesystem, completedpaths, ['start'], 'start')

        uniquepaths = {}
        for path in completedpaths:
            uniquepaths[path] = uniquepaths.get(path, 0) + 1

        return len(uniquepaths.keys())

class Dec12b(task.StrTask):
    def navigate(self, cavesystem, completedpaths, visitedcaves, currentcave, visittwice):
        for targetcave in cavesystem[currentcave]:
            if targetcave.islower() and targetcave in visitedcaves:
                if visittwice is not None and visittwice == targetcave:
                    self.navigate(cavesystem, completedpaths, [*visitedcaves, targetcave],
                                  targetcave, None)
            elif targetcave == 'end':
                completedpaths.append(','.join([*visitedcaves, targetcave]))
            else:
                self.navigate(cavesystem, completedpaths, [*visitedcaves, targetcave],
                              targetcave, visittwice)

    def run_list(self, data):
        cavesystem = {}
        for path in data:
            cave1, cave2 = path.split('-')
            cavesystem.setdefault(cave1, []).append(cave2)
            cavesystem.setdefault(cave2, []).append(cave1)

        smallcaves = sorted(filter(lambda x: x not in ('start', 'end') and x.islower(),
                                   cavesystem.keys()))

        completedpaths = []
        for smallcave in smallcaves:
            self.navigate(cavesystem, completedpaths, ['start'], 'start', smallcave)

        uniquepaths = {}
        for path in completedpaths:
            uniquepaths[path] = uniquepaths.get(path, 0) + 1

        return len(uniquepaths.keys())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec12a().run_tests_from_commandline()
        Dec12b().run_tests_from_commandline()
    else:
        Dec12a().runtests()
        Dec12b().runtests()
