#!/usr/bin/env python3

import task

class Board(object):
    def __init__(self, data):
        self.board = []
        self.marks = []
        for row in data:
            self.board.append(list(map(int, row.split())))
            self.marks.append([False] * len(self.board[-1]))

    def mark(self, num):
        for row_num, row in enumerate(self.board):
            for col_num, col in enumerate(row):
                if col == num:
                    self.marks[row_num][col_num] = True

    def get_unmarked_numbers(self):
        marked = []
        for row_num, row in enumerate(self.board):
            for col_num in range(len(row)):
                if self.marks[row_num][col_num] is False:
                    marked.append(self.board[row_num][col_num])
        return marked

    def has_bingo(self):
        for row_num in range(len(self.board)):
            if not False in self.marks[row_num]:
                return True

        for col_num in range(0, 5):
            if not False in map(lambda r, cn=col_num: r[cn], self.marks):
                return True

        return False

class dec04_1(task.StrTask):
    def run_list(self, data):
        draws = map(int, data[0].split(','))
        boards = []

        for i in range(0, int((len(data) - 1) / 6)):
            boards.append(Board(data[i * 6 + 2:i * 6 + 2 + 5]))

        for draw in draws:
            for board in boards:
                board.mark(draw)
                if board.has_bingo():
                    unmarked = board.get_unmarked_numbers()
                    return sum(unmarked) * draw
        return None

class dec04_2(task.StrTask):
    def run_list(self, data):
        draws = map(int, data[0].split(','))
        boards = []

        for i in range(0, int((len(data) - 1) / 6)):
            boards.append(Board(data[i * 6 + 2:i * 6 + 2 + 5]))

        for draw in draws:
            for board in boards:
                board.mark(draw)

            if len(boards) == 1 and boards[0].has_bingo():
                unmarked = boards[0].get_unmarked_numbers()
                return sum(unmarked) * draw

            boards = list(filter(lambda b: not b.has_bingo(), boards))

        return None

if __name__ == "__main__":
    dec04_1().runtests()
    dec04_2().runtests()
