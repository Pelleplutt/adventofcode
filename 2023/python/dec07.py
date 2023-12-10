#!/usr/bin/env python3

import pprint
import sys
import task
import functools

def card_rank_a(card):
    return 'AKQJT98765432'.index(card) + 1

def compare_hands_a(hand1, hand2):
    if hand1['type'] < hand2['type']:
        return -1
    elif hand1['type'] > hand2['type']:
        return 1
    else:
        for i in range(5):
            if card_rank_a(hand1['hand'][i]) < card_rank_a(hand2['hand'][i]):
                return -1
            if card_rank_a(hand1['hand'][i]) > card_rank_a(hand2['hand'][i]):
                return 1
    return 0

class Dec07a(task.StrTask):
    """
    """
    def hand_distr(self, hand, facit):
        h = {}
        for c in hand:
            h[c] = h.get(c, 0) + 1
        
        distr = list(reversed(sorted(h.values())))
        if len(distr) != len(facit):
            return False
        for i in range(len(distr)):
            if facit[i] != distr[i]:
                return False
            
        return True

    def identify_hand(self, s_hand):
        """
        Five of a kind, where all five cards have the same label: AAAAA
        Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        High card, where all cards' labels are distinct: 23456
        """

        if self.hand_distr(s_hand, [5]):
            return '1 five'
        elif self.hand_distr(s_hand, [4, 1]):
            return '2 four'
        elif self.hand_distr(s_hand, [3, 2]):
            return '3 fullhouse'
        elif self.hand_distr(s_hand, [3, 1, 1]):
            return '4 three'
        elif self.hand_distr(s_hand, [2, 2, 1]):
            return '5 two pair'
        elif self.hand_distr(s_hand, [2, 1, 1, 1]):
            return '6 pair'
        elif self.hand_distr(s_hand, [1, 1, 1, 1, 1]):
            return '7 high'
        else:
            print("Should not happen")

    def run_list(self, data):
        hands = []
        for d in data:
            hand, bet = d.split()

            hands += [{
                'hand': hand,
                'bet': int(bet),
                'type': self.identify_hand(hand)
            }]

        ordered_hands = sorted(hands, key=functools.cmp_to_key(compare_hands_a))
        hand_count = len(hands)
        winnings = 0
        for i in range(hand_count):
            winnings += (hand_count - i) * ordered_hands[i]['bet']

        return winnings
        
def card_rank_b(card):
    return 'AKQT98765432J'.index(card) + 1

def compare_hands_b(hand1, hand2):
    if hand1['type'] < hand2['type']:
        return -1
    elif hand1['type'] > hand2['type']:
        return 1
    else:
        for i in range(5):
            if card_rank_b(hand1['hand'][i]) < card_rank_b(hand2['hand'][i]):
                return -1
            if card_rank_b(hand1['hand'][i]) > card_rank_b(hand2['hand'][i]):
                return 1
    return 0

class Dec07b(task.StrTask):
    """
    """
    def hand_distr(self, hand, facit):
        if hand.find('J') > -1:
            for w in 'AKQT98765432':
                if self.hand_distr(hand.replace('J', w, 1), facit):
                    return True
        
        h = {}
        for c in hand:
            h[c] = h.get(c, 0) + 1
        
        distr = list(reversed(sorted(h.values())))
        if len(distr) != len(facit):
            return False
        for i in range(len(distr)):
            if facit[i] != distr[i]:
                return False
            
        return True

    def identify_hand(self, s_hand):
        if self.hand_distr(s_hand, [5]):
            return '1 five'
        elif self.hand_distr(s_hand, [4, 1]):
            return '2 four'
        elif self.hand_distr(s_hand, [3, 2]):
            return '3 fullhouse'
        elif self.hand_distr(s_hand, [3, 1, 1]):
            return '4 three'
        elif self.hand_distr(s_hand, [2, 2, 1]):
            return '5 two pair'
        elif self.hand_distr(s_hand, [2, 1, 1, 1]):
            return '6 pair'
        elif self.hand_distr(s_hand, [1, 1, 1, 1, 1]):
            return '7 high'
        else:
            print("Should not happen")

    def run_list(self, data):
        hands = []
        for d in data:
            hand, bet = d.split()

            hands += [{
                'hand': hand,
                'bet': int(bet),
                'type': self.identify_hand(hand)
            }]

        ordered_hands = sorted(hands, key=functools.cmp_to_key(compare_hands_b))
        hand_count = len(hands)
        winnings = 0
        for i in range(hand_count):
            winnings += (hand_count - i) * ordered_hands[i]['bet']

        return winnings

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec07a().run_tests_from_commandline()
        Dec07b().run_tests_from_commandline()
    else:
        Dec07a().runtests()
        Dec07b().runtests()
