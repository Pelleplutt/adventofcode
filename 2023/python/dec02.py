#!/usr/bin/env python3

import pprint
import sys
import task

class Dec02a(task.StrTask):
    """
    """
    def run_list(self, data):
        max_cubes = (12, 13, 14)
        total_sum = 0
        for game in data:
            game_possible = True
            game_id = int(game[game.index(' ') + 1:game.index(':')])

            turns = game[game.index(':') + 2:]

            for turn in turns.split(';'):
                for cube in turn.split(','):
                    count, color = cube.split()
                    count = int(count)
                    colndx = ['red' ,'green', 'blue'].index(color)
                    
                    if count > max_cubes[colndx]:
                        game_possible = False
                        break
                if not game_possible:
                    break
            
            if game_possible:
                total_sum += game_id
                
        return total_sum

class Dec02b(task.StrTask):
    """
    """
    def run_list(self, data):
        total_sum = 0
        for game in data:
            min_cubes = [None, None, None]
            turns = game[game.index(':') + 2:]

            for turn in turns.split(';'):
                for cube in turn.split(','):
                    count, color = cube.split()
                    count = int(count)
                    colndx = ['red' ,'green', 'blue'].index(color)
                    
                    if min_cubes[colndx] is None or min_cubes[colndx] < count:
                        min_cubes[colndx] = count

            total_sum += min_cubes[0] * min_cubes[1] * min_cubes[2]
                
        return total_sum

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec02a().run_tests_from_commandline()
        Dec02b().run_tests_from_commandline()
    else:
        Dec02a().runtests()
        Dec02b().runtests()
