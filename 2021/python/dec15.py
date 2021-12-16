#!/usr/bin/env python3

import sys
import task

def djikstra(costs, visited, distances, x, y, high_x, high_y):

    unvisited = []
    while not visited[high_y][high_x]:
        checks = []

        if x > 0 and not visited[y][x - 1]:
            checks.append([x - 1, y])

        if x < high_x and not visited[y][x + 1]:
            checks.append([x + 1, y])

        if y > 0 and not visited[y - 1][x]:
            checks.append([x, y - 1])

        if y < high_y and not visited[y + 1][x]:
            checks.append([x, y + 1])

        for check in checks:
            x2, y2 = check

            distance = distances[y][x] + costs[y2][x2]
            if distances[y2][x2] is None or distances[y2][x2] > distance:
                distances[y2][x2] = distance
            if [x2, y2] not in unvisited:
                unvisited.append([x2, y2])

        visited[y][x] = True

        unvisited = sorted(filter(lambda u: not visited[u[1]][u[0]], unvisited),
                           key=lambda x: distances[x[1]][x[0]])
        x, y = unvisited.pop(0)
        if not unvisited:
            break

class Dec15a(task.StrTask):
    """
    """

    def run_list(self, data):
        field = []
        visited = []
        scores = []
        high_x = len(data[0])
        high_y = len(data)


        for d in data:
            field.append(list(map(int, d)))
            visited.append([False] * high_x)
            scores.append([None] * high_x)

        scores[0][0] = 0
        djikstra(field, visited, scores, 0, 0, high_x - 1, high_y - 1)

        return scores[high_y - 1][high_x - 1]

class Dec15b(task.StrTask):
#class Dec15b(task.IntTask):
    """
    """
    def run_list(self, data):
        high_x = len(data[0])
        high_y = len(data)

        largefield = []
        for d in data:
            largefield.append(list(map(int, d)))

        for xmul in range(4):
            for y in range(high_y):
                for x in range(high_x):
                    risk = largefield[y][xmul * high_x + x] + 1
                    if risk > 9:
                        risk = 1
                    largefield[y].append(risk)

        for ymul in range(4):
            for y in range(high_y):
                nrow = []
                for x in range(high_x * 5):
                    risk = largefield[ymul * high_y + y][x] + 1
                    if risk > 9:
                        risk = 1
                    nrow.append(risk)
                largefield.append(nrow)

        high_x = len(largefield[0])
        high_y = len(largefield)

        visited = []
        scores = []
        for y in range(high_y):
            visited.append([False] * high_x)
            scores.append([None] * high_x)

        scores[0][0] = 0
        djikstra(largefield, visited, scores, 0, 0, high_x - 1, high_y - 1)

        return scores[high_y - 1][high_x - 1]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec15a().run_tests_from_commandline()
        Dec15b().run_tests_from_commandline()
    else:
        Dec15a().runtests()
        Dec15b().runtests()
