#!/usr/bin/env python3

import pprint
import sys
import task

class Dec04a(task.StrTask):
    """
    """
    def run_list(self, data):
        total_sum = 0
        for d in data:
            nums = d[d.index(':') + 2:]
            winners, mine = nums.split(' | ')
            winners = map(lambda x: int(x), winners.split())
            mine = map(lambda x: int(x), mine.split())

            m_map = {}
            for m in mine:
                m_map[m] = 1

            win_count = 0
            for w in winners:
                if m_map.get(w) is not None:
                    win_count += 1

            if win_count:
                total_sum += pow(2, win_count - 1)
                #print(f"win: {win_count}, {d}")

        return total_sum

class Dec04b(task.StrTask):
    def run_list(self, data):
        card_count = len(data)
        card_winnings = [[]] * len(data)

        for card_ndx in range(card_count):
            card = data[card_ndx]
            nums = card[card.index(':') + 2:]
            winners, mine = nums.split(' | ')
            winners = map(lambda x: int(x), winners.split())
            mine = map(lambda x: int(x), mine.split())

            m_map = {}
            for m in mine:
                m_map[m] = 1

            win_count = 0
            for w in winners:
                if m_map.get(w) is not None:
                    win_count += 1

            if card_ndx + win_count > card_count:
                card_winnings[card_ndx] = list(range(card_ndx + 1, card_count))
            else:
                card_winnings[card_ndx] = list(range(card_ndx + 1, card_ndx + win_count + 1))

        all_won_cards = [1] * card_count
        for card_ndx in range(card_count):
            for win in card_winnings[card_ndx]:
                all_won_cards[win] += all_won_cards[card_ndx]

        total_sum = 0
        for w in all_won_cards:
            total_sum += w

        return total_sum

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec04a().run_tests_from_commandline()
        Dec04b().run_tests_from_commandline()
    else:
        Dec04a().runtests()
        Dec04b().runtests()
