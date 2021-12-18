#!/usr/bin/env python3

import json
import math
import sys
import task

def finddigitright(data, startindex):
    digitlength = 1
    while startindex < len(data):
        if data[startindex].isdigit():
            while data[startindex + digitlength].isdigit():
                digitlength += 1

            return startindex, digitlength, \
                   int(data[startindex:startindex + digitlength])
        startindex += 1
    return None, None, None


def finddigitleft(data, startindex):
    digitlength = 1
    while startindex > 0:
        if data[startindex].isdigit():
            while data[startindex - digitlength].isdigit():
                digitlength += 1
            return startindex - digitlength + 1, digitlength, \
                   int(data[startindex - digitlength + 1:startindex + 1])
        startindex -= 1
    return None, None, None

def getsnailfishmagnitude(data):
    if isinstance(data[0], list):
        leftmagnitude = getsnailfishmagnitude(data[0])
    else:
        leftmagnitude = data[0]
    if isinstance(data[1], list):
        rightmagnitude = getsnailfishmagnitude(data[1])
    else:
        rightmagnitude = data[1]

    return leftmagnitude * 3 + rightmagnitude * 2

def addhomeworkpair(term1, term2):
    if term2 is not None:
        homework = f"[{term1},{term2}]"
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
                closingidx = homework.index(']', idx)
                addleft, addright = homework[idx:homework.index(']', idx)].split(',')

                rightdigitstart, rightdigitlength, rightdigit = finddigitright(homework, closingidx)
                if rightdigitstart is not None:
                    split = str(rightdigit + int(addright))
                    homework = homework[:rightdigitstart] + split + homework[rightdigitstart + rightdigitlength:]

                homework = homework[:idx - 1] + '0' + homework[closingidx + 1:]

                leftdigitstart, leftdigitlength, leftdigit = finddigitleft(homework, idx - 2)
                if leftdigitstart is not None:
                    split = str(leftdigit + int(addleft))
                    homework = homework[:leftdigitstart] + split + homework[leftdigitstart + leftdigitlength:]

                isexploaded = True
                break

        if not isexploaded:
            lastnumberidx = 0
            while True:
                rightdigitstart, rightdigitlength, rightdigit = finddigitright(homework, lastnumberidx)
                if rightdigit is None:
                    break
                if rightdigit >= 10:
                    split = f"[{math.floor(rightdigit / 2)},{math.ceil(rightdigit / 2)}]"
                    homework = homework[:rightdigitstart] + split + homework[rightdigitstart + rightdigitlength:]
                    issplit = True
                    break
                lastnumberidx = rightdigitstart + rightdigitlength

        if not isexploaded and not issplit:
            break

    return getsnailfishmagnitude(json.loads(homework)), homework


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
