import task
import re
import pprint
import sys

class dec04_1(task.str_task):
    def run_list(self, data):
        data.sort()
        shifts = {}

        guard = None
        sleepstart = None
        shift = None

        for l in data:
            m = re.match('\[....-..-.. ..:(..)\] (.*)', l)
            minute = int(m.group(1))
            action = m.group(2)

            if action[0] == 'G':
                guard = int(action[7:action.find(' beg')])
                shift = shifts.get(guard, [0] * 60)
            elif action[0] == 'f':
                sleepstart = minute
            elif action[0] == 'w':
                for mi in range(sleepstart, minute):
                    shift[mi] += 1
                shifts[guard] = shift
                sleepstart = None

        max_id = None
        max_slept = None
        max_slept_max_minute = None
        for id, shiftd in shifts.items():
            sleep = 0
            slept_max = shiftd[0]
            slept_max_minute = 0
            for minute in range(0, 60):
                minute_sleep = shiftd[minute]
                sleep += minute_sleep
                if minute_sleep > slept_max:
                    slept_max_minute = minute
                    slept_max = minute_sleep
            if max_slept is None or sleep > max_slept:
                max_id = id
                max_slept = sleep
                max_slept_max_minute =slept_max_minute
        return max_slept_max_minute * max_id        

class dec04_2(task.str_task):
    def run_list(self, data):
        data.sort()
        shifts = {}

        guard = None
        sleepstart = None
        shift = None

        for l in data:
            m = re.match('\[....-..-.. ..:(..)\] (.*)', l)
            minute = int(m.group(1))
            action = m.group(2)

            if action[0] == 'G':
                guard = int(action[7:action.find(' beg')])
                shift = shifts.get(guard, [0] * 60)
            elif action[0] == 'f':
                sleepstart = minute
            elif action[0] == 'w':
                for mi in range(sleepstart, minute):
                    shift[mi] += 1
                shifts[guard] = shift
                sleepstart = None

        max_id = None
        max_slept = None
        max_slept_max_minute = None
        for id, shiftd in shifts.items():
            for minute in range(0, 60):
                minute_sleep = shiftd[minute]
                if max_slept is None or minute_sleep > max_slept:
                    max_slept_max_minute = minute
                    max_slept = minute_sleep
                    max_id = id
        return max_slept_max_minute * max_id        


if __name__ == "__main__":
    dec04_1().runtests()
    dec04_2().runtests()
