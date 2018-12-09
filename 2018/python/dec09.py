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

    def list_insert(self, l, index, element):
        top_ndx = 0
        use_list = 0
        while use_list < len(l['lists']):
            top_ndx += len(l['lists'][use_list])
            if top_ndx > index:
                break
            use_list += 1

        base_ndx = top_ndx - len(l['lists'][use_list])
        l['lists'][use_list].insert(index - base_ndx, element)

        if len(l['lists'][use_list]) > 100000:
            l1 = l['lists'][use_list][:50000]
            l2 = l['lists'][use_list][50000:]
            l['lists'][use_list] = l1
            if use_list == len(l['lists']):
                l['lists'].append(l2)
            else:
                l['lists'].insert(use_list + 1, l2)
        l['len'] += 1

    def list_append(self, l, element):
        use_list = len(l['lists']) - 1
        l['lists'][use_list].append(element)
        l['len'] += 1

    def list_pop(self, l, index):
        top_ndx = 0
        use_list = 0
        while use_list < len(l['lists']):
            top_ndx += len(l['lists'][use_list])
            if top_ndx > index:
                break
            use_list += 1

        base_ndx = top_ndx - len(l['lists'][use_list])

        l['len'] -= 1
        return l['lists'][use_list].pop(index - base_ndx)

    def list_len(self, l):
        return l['len']

    def run_list(self, data):
        player_count = data[0]
        last_marble = data[1]

        player_scores = [0] * player_count
        current_marble = 0
        playfield = {
            'len': 1,
            'lists': [[0]]
        }
        
        for marble in range(1, last_marble + 1):
            playfield_size = self.list_len(playfield)
            current_player = marble % player_count
            if last_marble > 0 and marble % 23 == 0:
                player_scores[current_player] += marble
                remove_marble = (current_marble - 7)
                if remove_marble < 0:
                    remove_marble = playfield_size + remove_marble
                player_scores[current_player] += self.list_pop(playfield, remove_marble)
                current_marble = remove_marble
                if remove_marble == playfield_size:
                    current_marble = 0
            else:
                insert_pos = current_marble + 2
                if insert_pos > playfield_size:
                    insert_pos = 1

                if insert_pos == playfield_size:
                    self.list_append(playfield, marble)
                    current_marble = marble
                else:
                    self.list_insert(playfield, insert_pos, marble)
                    current_marble = insert_pos

        return max(player_scores)

if __name__ == "__main__":
    dec09_1().runtests()
    dec09_2().runtests()
