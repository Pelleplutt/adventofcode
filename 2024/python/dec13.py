#!/usr/bin/env python3

import pprint
import sys
import task

a_price = 3
b_price = 1

class Dec13(task.Task):
    def parse(self, rawdata):
        data = []
        while rawdata:
            while len(rawdata[-1]) == 0:
                rawdata.pop()
            price = rawdata.pop()[7:].split(', ')
            bb = rawdata.pop()[10:].split(', ')
            ba = rawdata.pop()[10:].split(', ')

            data.append({
                'A': [int(ba[0][1:]), int(ba[1][1:])],
                'B': [int(bb[0][1:]), int(bb[1][1:])],
                'price': [int(price[0][2:]), int(price[1][2:])],
            })

        return data

class Dec13a(Dec13):
    def run(self, games):
        cost = 0
        for game in games:
            ba = game['A']
            bb = game['B']
            price = game['price']
            # In most cases optimizing for pressing B is the right answer, assert when this is not the case
            if ba[0] > 3 * bb[0] and  ba[1] > 3 * bb[1]:
                raise AssertionError('Not optimal solution')

            # minimum of multiples of B in either X or Y is the max times we can press B
            max_b_presses = min(int(price[0] / bb[0]), int(price[1] / bb[1]))

            for b_press in range(max_b_presses, 0, -1):
                x = price[0] - b_press * bb[0]
                y = price[1] - b_press * bb[1]

                a_press_x = x / ba[0]
                a_press_y = y / ba[1]

                if b_press <= 100 and int(a_press_x) <= 100 and a_press_x == a_press_y and x % ba[0] == 0 and y % ba[1] == 0:
                    cost += b_press * b_price + int(a_press_x) * a_price
                    break

        return cost


class Dec13b(Dec13):
    def run(self, games):
        cost = 0
        for game in games:
            ba = game['A']
            bb = game['B']
            price = game['price']
            price[0] += 10000000000000
            price[1] += 10000000000000
            #print(f"  Game ({price})  A={ba}, B={bb}")

            # minimum of multiples of A in either X or Y is the max times we can press A, same for B
            max_b_presses = min(int(price[0] / bb[0]), int(price[1] / bb[1]))
            max_a_presses = min(int(price[0] / ba[0]), int(price[1] / ba[1]))

            # In most cases optimizing for pressing B is the right answer, assert when this is not the case
            if ba[0] > 3 * bb[0] and  ba[1] > 3 * bb[1]:
                raise AssertionError('Not optimal solution')

            remainder_x = price[0] - max_b_presses * bb[0]
            remainder_y = price[1] - max_b_presses * bb[1]


            print(f"{price} A={ba} B={bb} maxB=={max_b_presses}, remainder at maxB=({remainder_x}, {remainder_y})")
            # Possible solutions are remainder + n * B is divisible by A, we need to find the smallest n for this
            # x = n1 * Ax + n2 * Bx
            # y = n1 * Ay + n2 * By
            # 
            # Typical outcome at maximum B presses are:
            # [10000000009475, 10000000004041] A=[35, 17] B=[37, 66] maxB==151515151576, remainder at maxB=(4393939401163, 25)
            # Decreasing number of presses on B means BOTH numbers for the remainders increase by Bx,By respectively. 
            # So solution will never be less than (4393939401163 / Ax) (==125541125747) times that we need to press A button.

            # There is no way we can find a solution to this where we do not press A at least (4393939401163 / Ax) times. 
            # Start of check is therefore 
            # n = int(4393939401163 / Ax)
            # 4393939401163 + , 25
            
            if remainder_y < remainder_x:
                for n in range(max_a_presses):
                    ry = remainder_y + n * bb[1]
                    if ry % ba[1] == 0:
                        rx = remainder_x + n * bb[0]
                        a_press_x = rx / ba[0]
                        a_press_y = ry / ba[1]
                        if rx % ba[0] == 0 and a_press_x == a_press_y:
                            b_press = max_b_presses - n
                            print(f"  Solve ({price[0]},{price[1]}) -> {a_press_x}xA, {b_press}xB")
                            cost += b_press * b_price + int(a_press_x) * a_price
                            break
            else:
                for n in range(max_a_presses):
                    rx = remainder_x + n * bb[0]
                    if rx % ba[0] == 0:
                        ry = remainder_y + n * bb[1]
                        a_press_x = rx / ba[0]
                        a_press_y = ry / ba[1]
                        if rx % ba[0] == 0 and a_press_x == a_press_y:
                            b_press = max_b_presses - n
                            print(f"  Solve ({price[0]},{price[1]}) -> {a_press_x}xA, {b_press}xB")
                            cost += b_press * b_price + int(a_press_x) * a_price
                            break
        return cost

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec13a().run_specific_tests(sys.argv[1:])
        Dec13b().run_specific_tests(sys.argv[1:])
    else:
        Dec13a().runtests()
        Dec13b().runtests()
