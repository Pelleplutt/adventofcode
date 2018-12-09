import task
import pprint
from blist import blist

class dec09_1(task.IntTask):

    def print_playfield(self, marble, current_marble, playfield):
        s = '[{0}] '.format(marble)
        for i in range(len(playfield)):
            if i > 0:
                s += ', '
            if i == current_marble:
                s += '({0})'.format(playfield[i])
            else:
                s += '{0}'.format(playfield[i])
        print(s)

    def run_list(self, data):
        player_count = data[0]
        last_marble = data[1]

        player_scores = [0] * player_count
        current_marble = 0
        playfield = blist([0])
        
        for marble in range(1, last_marble + 1):
            playfield_size = len(playfield)
            current_player = marble % player_count
            if last_marble > 0 and marble % 23 == 0:
                player_scores[current_player] += marble
                remove_marble = (current_marble - 7)
                if remove_marble < 0:
                    remove_marble = playfield_size + remove_marble
                player_scores[current_player] += playfield.pop(remove_marble)
                current_marble = remove_marble
                if remove_marble == playfield_size:
                    current_marble = 0
            else:
                insert_pos = current_marble + 2
                if insert_pos > playfield_size:
                    insert_pos = 1

                if insert_pos == playfield_size:
                    playfield.append(marble)
                    current_marble = marble
                else:
                    playfield.insert(insert_pos, marble)
                    current_marble = insert_pos

        return max(player_scores)


class dec09_2(task.IntTask):
    def run_list(self, data):
        first = dec09_1()
        return first.run_list(data)

if __name__ == "__main__":
    dec09_1().runtests()
    dec09_2().runtests()
