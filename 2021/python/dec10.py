#!/usr/bin/env python3

import sys
import task

STATEMENTS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


class Dec10a(task.StrTask):
    """
    """
    missing_token_points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    def parse(self, line, closing=None):
        while line:
            token = line.pop(0)
            if STATEMENTS.get(token) is not None:
                subtoken = self.parse(line, STATEMENTS[token])
                if subtoken is not None:
                    return subtoken
            elif closing is not None and token == closing:
                return None
            else:
                return token
        return None

    def run_list(self, data):
        total_points = 0
        for line in data:
            token = self.parse(list(line))
            if token is not None:
                total_points += Dec10a.missing_token_points[token]
        return total_points



class Dec10b(task.StrTask):
    """
    """
    closing_token_points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    def run_list(self, data):
        line_points = []
        for line in data:
            missing_tokens = []
            for token in line:
                if STATEMENTS.get(token) is not None:
                    missing_tokens.insert(0, STATEMENTS[token])
                elif missing_tokens and missing_tokens[0] == token:
                    missing_tokens.pop(0)
                else:
                    missing_tokens = []
                    break

            if missing_tokens:
                missing_token_points = 0
                for token in missing_tokens:
                    missing_token_points = missing_token_points * 5 + Dec10b.closing_token_points[token]
                line_points.append(missing_token_points)

        line_points = sorted(line_points)
        return line_points[int(len(line_points) / 2)]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec10a().run_tests_from_commandline()
        Dec10b().run_tests_from_commandline()
    else:
        Dec10a().runtests()
        Dec10b().runtests()
