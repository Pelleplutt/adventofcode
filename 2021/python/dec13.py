#!/usr/bin/env python3

import sys
import task

class Dec13a(task.StrTask):
    """
    """

    def run_list(self, data):

        folds = []
        dots = []
        for d in data:
            try:
                x, y = d.split(',')
                dots.append([int(x), int(y)])
            except ValueError:
                if len(d):
                    folds.append([d[11], int(d[13:])])

        for fold in folds[0:1]:
            if fold[0] == 'x':
                for dot in dots:
                    if dot[0] > fold[1]:
                        dot[0] = fold[1] - (dot[0] - fold[1])
            else:
                for dot in dots:
                    if dot[1] > fold[1]:
                        dot[1] = fold[1] - (dot[1] - fold[1])

        udots = {}
        for dot in dots:
            udots[','.join(map(str, dot))] = 1

        return len(udots)


class Dec13b(task.StrTask):
    """
    """
    def run_list(self, data):

        folds = []
        dots = []
        for d in data:
            try:
                x, y = d.split(',')
                dots.append([int(x), int(y)])
            except ValueError:
                if len(d):
                    folds.append([d[11], int(d[13:])])

        for fold in folds:
            if fold[0] == 'x':
                for dot in dots:
                    if dot[0] > fold[1]:
                        dot[0] = fold[1] - (dot[0] - fold[1])
            else:
                for dot in dots:
                    if dot[1] > fold[1]:
                        dot[1] = fold[1] - (dot[1] - fold[1])

        maxx = max(map(lambda d: d[0], dots))
        maxy = max(map(lambda d: d[1], dots))

        result = ['.' * (maxx + 1)] * (maxy + 1)
        for dot in dots:
            result[dot[1]] = result[dot[1]][:dot[0]] + '#' + result[dot[1]][dot[0] + 1:]

        return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec13a().run_tests_from_commandline()
        Dec13b().run_tests_from_commandline()
    else:
        Dec13a().runtests()
        Dec13b().runtests()
