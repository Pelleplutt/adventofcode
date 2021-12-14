#!/usr/bin/env python3

import sys
import task

class Dec14a(task.StrTask):
    """
    """
    def run_list(self, data):
        template = data[0]

        rules = {}
        for d in data[2:]:
            frompolymer, topolymer = d.split(' -> ')
            rules[frompolymer] = topolymer

        polymer = template
        for step in range(10):
            newpolymer = template[0]
            for pos in range(len(polymer) - 1):
                new = polymer[pos] + polymer[pos + 1]
                newpolymer += rules[new] + polymer[pos + 1]
            polymer = newpolymer

        elements = {}
        for i in range(len(polymer)):
            elements[polymer[i]] = elements.get(polymer[i], 0) + 1

        most_common = max(elements, key=elements.get)
        least_common = min(elements, key=elements.get)

        return elements[most_common] - elements[least_common]


class Dec14b(task.StrTask):
    """
    """
    def run_list(self, data):
        template = data[0]

        rules = {}
        for d in data[2:]:
            frompolymer, topolymer = d.split(' -> ')
            rules[frompolymer] = topolymer

        # Switch to represnting the input polymer as a count of element pairs
        # instead. Keeping the element pair and a counter prevents this from
        # growing out of control.
        polymerpairs = {}
        for pos in range(len(template) - 1):
            polymer = template[pos] + template[pos + 1]
            polymerpairs[polymer] = polymerpairs.get(polymer, 0) + 1

        for step in range(40):
            newpolymerpairs = {}
            for polymer in polymerpairs:
                newpolymer1 = polymer[0] + rules[polymer]
                newpolymer2 = rules[polymer] + polymer[1]
                # If we have added this element pair to the new polymer before,
                # increase the counter, otherwise fall back to the input
                # counter from the pair we used to trigger the rule
                newpolymerpairs[newpolymer1] = newpolymerpairs.get(newpolymer1, 0) + \
                                               polymerpairs.get(polymer, 0)
                newpolymerpairs[newpolymer2] = newpolymerpairs.get(newpolymer2, 0) + \
                                               polymerpairs.get(polymer, 0)

            polymerpairs = newpolymerpairs

        elements = {}
        # Sum the occurencies of the first char only in the pairs as each char
        # is always present in two pairs..
        for k in polymerpairs:
            elements[k[0]] = elements.get(k[0], 0) + polymerpairs[k]
        # ... then add the last one as this is never counted otherwise.
        # The last is always the same char as the last in the input
        elements[template[-1]] += 1

        most_common = max(elements, key=elements.get)
        least_common = min(elements, key=elements.get)

        return elements[most_common] - elements[least_common]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec14a().run_tests_from_commandline()
        Dec14b().run_tests_from_commandline()
    else:
        Dec14a().runtests()
        Dec14b().runtests()
