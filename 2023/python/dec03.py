#!/usr/bin/env python3

import pprint
import sys
import task

class Dec03a(task.StrTask):
    """
    """
    def is_symbol(self, sym):
        return '0123456789.'.find(sym) == -1
    
    def symbol_adj(self, data, row_ndx, total_rows, col_ndx, total_cols):
        if row_ndx > 0:
            if (self.is_symbol(data[row_ndx - 1][col_ndx]) or
               (col_ndx > 0 and self.is_symbol(data[row_ndx - 1][col_ndx - 1])) or
               (col_ndx + 1 < total_cols and self.is_symbol(data[row_ndx - 1][col_ndx + 1]))):
                return True
        if row_ndx + 1 < total_rows:
            if (self.is_symbol(data[row_ndx + 1][col_ndx]) or
               (col_ndx > 0 and self.is_symbol(data[row_ndx + 1][col_ndx - 1])) or
               (col_ndx + 1 < total_cols and self.is_symbol(data[row_ndx + 1][col_ndx + 1]))):
                return True
        if ((col_ndx > 0 and self.is_symbol(data[row_ndx][col_ndx - 1])) or
            (col_ndx + 1 < total_cols and self.is_symbol(data[row_ndx][col_ndx + 1]))):
            return True

        return False       

    def run_list(self, data):
        
        total_sum = 0
        total_rows = len(data)
        total_cols = len(data[0])
        for row_ndx in range(total_rows):
            num = ''
            sym_adj = False
            for col_ndx in range(total_cols):
                if data[row_ndx][col_ndx].isdigit():
                    num += data[row_ndx][col_ndx]
                    if sym_adj or self.symbol_adj(data, row_ndx, total_rows, col_ndx, total_cols):
                        sym_adj = True
                else:
                    if sym_adj:
                        total_sum += int(num)
                        #print(f"num: {num}, row: {row_ndx}, col: {col_ndx}")
                    num = ''
                    sym_adj = False

            if sym_adj:
                #print(f"num: {num}, row: {row_ndx}, col: {col_ndx}")
                total_sum += int(num)

        return total_sum

class Dec03b(task.StrTask):
#class Dec03b(task.IntTask):
    """
    """
    def is_symbol(self, sym):
        return '0123456789.'.find(sym) == -1
    
    def add_sym_adj(self, sym_adj, row, col):
        sym_adj[f"{row}x{col}"] = 1
    
    def symbol_adj(self, data, sym_adj, row_ndx, total_rows, col_ndx, total_cols):
        modif = [
            (-1, 0), (-1, -1), (-1, 1),
            (0, -1), (0, 1),
            (1, 0), (1, -1), (1, 1)
        ]

        for m in modif:
            r, c = row_ndx + m[0], col_ndx + m[1]
            if r > 0 and r < total_rows and c > 0 and c < total_cols and self.is_symbol(data[r][c]):
               self.add_sym_adj(sym_adj, r, c)
        
        return sym_adj
    
    def add_all_sym_adj(self, all_sym_adj, sym_adj, num):
        num = int(num)
        #print(f"Add all sym {num}")
        for k in sym_adj.keys():
            if all_sym_adj.get(k) is not None:
                all_sym_adj[k].append(num)
            else:
                all_sym_adj[k] = [num]

    def run_list(self, data):
        total_rows = len(data)
        total_cols = len(data[0])
        all_sym_adj = {}
        for row_ndx in range(total_rows):
            num = ''
            sym_adj = {}
            for col_ndx in range(total_cols):
                if data[row_ndx][col_ndx].isdigit():
                    num += data[row_ndx][col_ndx]
                    self.symbol_adj(data, sym_adj, row_ndx, total_rows, col_ndx, total_cols)
                else:
                    if len(num):
                        self.add_all_sym_adj(all_sym_adj, sym_adj, num)
                    num = ''
                    sym_adj = {}

            if len(num):
                self.add_all_sym_adj(all_sym_adj, sym_adj, num)
        
        total_sum = 0

        for k, v in all_sym_adj.items():
            if len(v) == 2:
                total_sum += v[0] * v[1]

        return total_sum

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec03a().run_tests_from_commandline()
        Dec03b().run_tests_from_commandline()
    else:
        Dec03a().runtests()
        Dec03b().runtests()
