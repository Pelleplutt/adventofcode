#!/usr/bin/env python3

import pprint
import sys
import task

class Dec05a(task.StrTask):
    def _valid(self, update):
        for ndx, num in enumerate(update):
            if self.rules.get(num, set()).intersection(set(update[:ndx])):
                return False

        return True

    def run_list(self, data):
        self.rules = {}
        updates = []
        for row in data:
            if '|' in row:
                l, r = row.split('|')
                l = int(l)
                if self.rules.get(l) is not None:
                    self.rules[l].add(int(r))
                else:
                    self.rules[l] = set([int(r)])
            elif ',' in row:
                updates.append(list(map(lambda x: int(x), row.split(','))))

        sum = 0
        for update in updates:
            if self._valid(update):
                sum += update[int(len(update) / 2)]
        return sum

               

class Dec05b(task.StrTask):
    def _valid(self, update):
        for ndx, num in enumerate(update):
            if self.rules.get(num, set()).intersection(set(update[:ndx])):
                return False

        return True

    def run_list(self, data):
        self.rules = {}
        updates = []
        for row in data:
            if '|' in row:
                l, r = row.split('|')
                l = int(l)
                if self.rules.get(l) is not None:
                    self.rules[l].add(int(r))
                else:
                    self.rules[l] = set([int(r)])
            elif ',' in row:
                updates.append(list(map(lambda x: int(x), row.split(','))))

        sum = 0
        for update in updates:
            valid = self._valid(update)
            if not valid:
                while not valid:
                    left = []
                    for ndx, num in enumerate(update):
                        br = False
                        rule = self.rules.get(num)
                        if rule is None:
                            left.append(num)
                            continue

                        for offender_ndx, offender in enumerate(left):
                            if offender in rule:
                                update = [*left[:offender_ndx], num, *left[offender_ndx:], *update[ndx + 1:]]
                                br = True
                                break

                        if br:
                            break

                        left.append(num)
                    valid = self._valid(update)

                sum += update[int(len(update) / 2)]
        return sum

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec05a().run_tests_from_commandline()
        Dec05b().run_tests_from_commandline()
    else:
        Dec05a().runtests()
        Dec05b().runtests()
