#!/usr/bin/env python3

import pprint
import sys
import task

class Dec01a(task.StrTask):
    """
    """
    def run_list(self, data):
        total = 0
        for d in data:
            for n in d:
                if n.isdigit():
                    f = n
                    break
            for n in reversed(d):
                if n.isdigit():
                    l = n
                    break

            total += int(f + l)
        return total


class Dec01b(task.StrTask):
    """
    """
    def run_list(self, data):
        number_str = [
            'zero',
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine'
        ]
        rev_number_str = [''.join(list(reversed(d))) for d in number_str]

        total = 0
        for d in data:
            fdigitpos = None
            ldigitpos = None
            for pos in range(len(d)):
                if d[pos].isdigit():
                    fdigitpos = pos
                    fdigit = int(d[pos])
                    break

            for numstr_ndx in range(10):
                pos = d.find(number_str[numstr_ndx])
                if pos > -1 and (fdigitpos is None or pos < fdigitpos):
                    fdigitpos = pos
                    fdigit = numstr_ndx

            d = ''.join(reversed(d))

            for pos in range(len(d)):
                if d[pos].isdigit():
                    ldigitpos = pos
                    ldigit = int(d[pos])
                    break

            for numstr_ndx in range(10):
                pos = d.find(rev_number_str[numstr_ndx])
                if pos > -1 and (ldigitpos is None or pos < ldigitpos):
                    ldigitpos = pos
                    ldigit = numstr_ndx
            
            total += fdigit * 10 + ldigit
            #print(f"total: {total}, fdigit: {fdigit}, fdigitpos: {fdigitpos}, ldigit: {ldigit}, ldigitpos: {ldigitpos}, str: {d}")

        return total


if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec01a().run_tests_from_commandline()
        Dec01b().run_tests_from_commandline()
    else:
        Dec01a().runtests()
        Dec01b().runtests()
