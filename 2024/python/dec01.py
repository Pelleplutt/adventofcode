#!/usr/bin/env python3

import pprint
import sys
import task

class Dec01a(task.StrTask):
    """
    """
    def run_list(self, data):
        llist, rlist = [], []

        for ndx, row in enumerate(data):
            l, r = map(lambda x: int(x), row.split())
            llist.append(l)
            rlist.append(r)

        order_llist = list(sorted(llist, reverse=True))
        order_rlist = list(sorted(rlist, reverse=True))

        sum = 0
        for i in range(len(order_llist)):
            li = order_llist[i]
            ri = order_rlist[i]
            sum += abs(li - ri)

        return sum



class Dec01b(task.StrTask):
    def run_list(self, data):
        llist, rlist = [], {}

        for ndx, row in enumerate(data):
            l, r = map(lambda x: int(x), row.split())
            llist.append(l)
            rlist[r] = rlist.get(r, 0) + 1

        sum = 0
        for i in range(len(llist)):
            sum += llist[i] * rlist.get(llist[i], 0)

        return sum

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec01a().run_tests_from_commandline()
        Dec01b().run_tests_from_commandline()
    else:
        Dec01a().runtests()
        Dec01b().runtests()
