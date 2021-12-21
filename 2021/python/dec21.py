#!/usr/bin/env python3

import sys
import task

class Dec21a(task.StrTask):
    """
    """

    def run_list(self, data):
        p1_position, p2_position = int(data[0][28:]) - 1, int(data[1][28:]) - 1
        p1_score, p2_score = 0, 0

        dice = 0
        rolls = 0
        while True:
            p1_position = (p1_position + dice * 3 + 6) % 10
            p2_position = (p2_position + dice * 3 + 15) % 10
            dice += 6
            rolls += 6

            p1_score += p1_position + 1
            if p1_score >= 1000:
                return (rolls - 3) * p2_score
            p2_score += p2_position + 1
            if p2_score >= 1000:
                return rolls * p1_score                

# All the possible rolls from a 3-dice, also the frequency of
# occurences, given it is from three rolls.

DIRAC_SUMS = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]


class Dec21b(task.StrTask):
    """
    """

    def play_dirac(self, p1_position, p2_position, p1_score, p2_score, cache):
        cache_key = (p1_position, p2_position, p1_score, p2_score)
        if cache.get(cache_key):
            return cache[cache_key]

        sum_p1_wins = 0
        sum_p2_wins = 0

        if p1_score >= 21:
            sum_p1_wins += 1
        elif p2_score >= 21:
            sum_p2_wins += 1
        else:
            for roll, freq in DIRAC_SUMS:
                new_p1_position = (p1_position + roll) % 10
                new_p1_score = p1_score + new_p1_position + 1

                p2_wins, p1_wins = self.play_dirac(p2_position, new_p1_position,
                                                   p2_score, new_p1_score,
                                                   cache)
                sum_p1_wins += p1_wins * freq
                sum_p2_wins += p2_wins * freq

        cache[cache_key] = (sum_p1_wins, sum_p2_wins)
        return sum_p1_wins, sum_p2_wins

    def run_list(self, data):
        p1_position, p2_position = int(data[0][28:]) - 1, int(data[1][28:]) - 1

        cache = {}
        p1_wins, p2_wins = self.play_dirac(p1_position, p2_position, 0, 0, cache)
        return p1_wins if p1_wins > p2_wins else p2_wins

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec21a().run_tests_from_commandline()
        Dec21b().run_tests_from_commandline()
    else:
        Dec21a().runtests()
        Dec21b().runtests()
