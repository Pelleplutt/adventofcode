#!/usr/bin/env python3

import math
import sys
import task

def finddigitright(data, startindex):
    while startindex < len(data):
        if type(data[startindex]) == int:
            return startindex
        startindex += 1
    return None

def finddigitleft(data, startindex):
    while startindex > 0:
        if type(data[startindex]) == int:
            return startindex
        startindex -= 1
    return None

def getsnailfishmagnitude(data, idx):
    if data[idx] == '[':
        leftmagnitude, idx = getsnailfishmagnitude(data, idx + 1)
    else:
        leftmagnitude = data[idx]
        idx += 1

    if data[idx] == '[':
        rightmagnitude, idx = getsnailfishmagnitude(data, idx + 1)
    else:
        rightmagnitude = data[idx]
        idx += 1
    return leftmagnitude * 3 + rightmagnitude * 2, idx + 1

def parsehomeworkstr(data):
    homework, digitbuildup = [], ''
    for idx, char in enumerate(data):
        if char in ('[', ']'):
            if digitbuildup:
                homework.append(int(digitbuildup))
                digitbuildup = ''
            homework.append(char)
        if char.isdigit():
            digitbuildup += char
        elif char == ',':
            if digitbuildup:
                homework.append(int(digitbuildup))
                digitbuildup = ''
    
    return homework

def addhomeworkpair(term1, term2):
    if type(term1) == str:
        term1 = parsehomeworkstr(term1)

    if term2 is not None:
        homework = ['['] + term1 + parsehomeworkstr(term2) + [']']
    else:
        homework = term1

    while True:
        isexploaded, issplit = False, False

        nesteddepth = 0
        for idx, char in enumerate(homework):
            if char == '[':
                nesteddepth += 1
            elif char == ']':
                nesteddepth -= 1
            elif nesteddepth > 4:

                addleft, addright = homework[idx], homework[idx + 1]

                rightdigitidx = finddigitright(homework, idx + 2)
                if rightdigitidx is not None:
                    homework[rightdigitidx] += addright
                del homework[idx - 1:idx + 3]
                homework.insert(idx - 1, 0)

                leftdigitidx = finddigitleft(homework, idx - 2)
                if leftdigitidx is not None:
                    homework[leftdigitidx] += addleft
                
                isexploaded = True
                break

        if not isexploaded:
            lastnumberidx = 0
            while True:
                rightdigitidx = finddigitright(homework, lastnumberidx)
                if rightdigitidx is None:
                    break
                if homework[rightdigitidx] >= 10:
                    homework = homework[:rightdigitidx] + \
                        ['[', math.floor(homework[rightdigitidx] / 2), math.ceil(homework[rightdigitidx] / 2), ']' ] +\
                        homework[rightdigitidx + 1:]

                    issplit = True
                    break
                lastnumberidx = rightdigitidx + 1

        if not isexploaded and not issplit:
            break

    return getsnailfishmagnitude(homework, 1)[0], homework


class Dec18a(task.StrTask):
    """
    """
    def run_list(self, data):
        homework = data.pop(0)
        magnitude = 0

        while True:
            magnitude, homework = addhomeworkpair(homework, data.pop(0) if data else None)
            if not data:
                break

        return magnitude

class Dec18b(task.StrTask):
    """
    """
    
    def run_list(self, data):


        additionpairs = []
        if len(data) > 1:
            for idx1, d1 in enumerate(data):
                for idx2, d2 in enumerate(data):
                    if d1 != d2:
                        additionpairs.append([data[idx1], data[idx2]])
        else:
            additionpairs.append([data[0], None])

        maxmagnitude = 0
        for additionpair in additionpairs:
            magnitude, homework = addhomeworkpair(*additionpair)
            if magnitude > maxmagnitude:
                maxmagnitude = magnitude

        return maxmagnitude


if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec18a().run_tests_from_commandline()
        Dec18b().run_tests_from_commandline()
    else:
        Dec18a().runtests()
        Dec18b().runtests()
