import task

class dec01_1(task.str_task):
    """
    You're standing in a room with "digitization quarantine" written in LEDs
    along one wall. The only door is locked, but it includes a small interface.
    "Restricted Area - Strictly No Digitized Users Allowed."

    It goes on to explain that you may only leave by solving a captcha to prove
    you're not a human. Apparently, you only get one millisecond to solve the
    captcha: too fast for a normal human, but it feels like hours to you.

    The captcha requires you to review a sequence of digits (your puzzle input)
    and find the sum of all digits that match the next digit in the list. The
    list is circular, so the digit after the last digit is the first digit in
    the list.

    For example:

        1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
        1111 produces 4 because each digit (all 1) matches the next.
        1234 produces 0 because no digit matches the next.
        91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
        What is the solution to your captcha?
    """
    def run(self, data):
        sum = 0
        if len(data) > 1:
            for idx, d in enumerate(data):
                if data[idx - 1] == d:
                    sum = sum + int(d)
        return sum

class dec01_2(task.str_task):
    """
    You notice a progress bar that jumps to 50% completion. Apparently, the
    door isn't yet satisfied, but it did emit a star as encouragement. The
    instructions change:

    Now, instead of considering the next digit, it wants you to consider the
    digit halfway around the circular list. That is, if your list contains 10
    items, only include a digit in your sum if the digit 10/2 = 5 steps forward
    matches it. Fortunately, your list has an even number of elements.

    For example:

        1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
        1221 produces 0, because every comparison is between a 1 and a 2.
        123425 produces 4, because both 2s match each other, but no other digit has a match.
        123123 produces 12.
        12131415 produces 4.
        What is the solution to your new captcha?
    """
    def run(self, data):
        sum = 0
        half = int(len(data) / 2)
        for idx, d in enumerate(data[:half]):
            if d == data[half + idx]:
                sum = sum + int(d) * 2
        return sum

if __name__ == "__main__":
    dec01_1().runtests()
    dec01_2().runtests()
