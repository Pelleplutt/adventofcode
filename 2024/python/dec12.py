#!/usr/bin/env python3

import pprint
import sys
import task

class Dec12(task.Task):
    def _expand_plot(self, garden, plant, x, y, maxx, maxy, plotcoords):
        plotcoords.add(f"{x},{y}")
        if x > 0 and garden[y][x - 1] == plant and f"{x - 1},{y}" not in plotcoords:
            self._expand_plot(garden, plant, x - 1, y, maxx, maxy, plotcoords)
        if x + 1 < maxx and garden[y][x + 1] == plant and f"{x + 1},{y}" not in plotcoords:
            self._expand_plot(garden, plant, x + 1, y, maxx, maxy, plotcoords)
        if y > 0 and garden[y - 1][x] == plant and f"{x},{y - 1}" not in plotcoords:
            self._expand_plot(garden, plant, x, y - 1, maxx, maxy, plotcoords)
        if y + 1 < maxy and garden[y + 1][x] == plant and f"{x},{y + 1}" not in plotcoords:
            self._expand_plot(garden, plant, x, y + 1, maxx, maxy, plotcoords)

class Dec12a(Dec12):
    def _get_price(self, plotcoords):
        perim = 0
        for c in plotcoords:
            x, y = map(int, c.split(','))

            if f"{x + 1},{y}" not in plotcoords:
                perim += 1
            if f"{x - 1},{y}" not in plotcoords:
                perim += 1
            if f"{x},{y - 1}" not in plotcoords:
                perim += 1
            if f"{x},{y + 1}" not in plotcoords:
                perim += 1

        return perim * len(plotcoords)

    def run(self, garden):
        maxy = len(garden)
        maxx = len(garden[0])
        
        allplotcoords = set()
        price = 0
        for y in range(maxy):
            for x, plant in enumerate(garden[y]):
                if f"{x},{y}" not in allplotcoords:
                    plotcoords = set()
                    self._expand_plot(garden, plant, x, y, maxx, maxy, plotcoords)
                    price += self._get_price(plotcoords)
                    allplotcoords.update(plotcoords)

        return price

class Dec12b(Dec12):
    def _expand_edge(self, x, y, maxx, maxy, edge, plotcoords, alledges):
        alledges.add(f"{x},{y},{edge}")

        if edge == 'l':
            if f"{x},{y - 1}" in plotcoords and f"{x - 1},{y - 1}" not in plotcoords and f"{x},{y - 1},{edge}" not in alledges:
                self._expand_edge(x, y - 1, maxx, maxy, edge, plotcoords, alledges)
            if f"{x},{y + 1}" in plotcoords and f"{x - 1},{y + 1}" not in plotcoords and f"{x},{y + 1},{edge}" not in alledges:
                self._expand_edge(x, y + 1, maxx, maxy, edge, plotcoords, alledges)
        elif edge == 'r':
            if f"{x},{y - 1}" in plotcoords and f"{x + 1},{y - 1}" not in plotcoords and f"{x},{y - 1},{edge}" not in alledges:
                self._expand_edge(x, y - 1, maxx, maxy, edge, plotcoords, alledges)
            if f"{x},{y + 1}" in plotcoords and f"{x + 1},{y + 1}" not in plotcoords and f"{x},{y + 1},{edge}" not in alledges:
                self._expand_edge(x, y + 1, maxx, maxy, edge, plotcoords, alledges)
        elif edge == 'u':
            if f"{x - 1},{y}" in plotcoords and f"{x - 1},{y - 1}" not in plotcoords and f"{x - 1},{y},{edge}" not in alledges:
                self._expand_edge(x - 1, y, maxx, maxy, edge, plotcoords, alledges)
            if f"{x + 1},{y}" in plotcoords and f"{x + 1},{y - 1}" not in plotcoords and f"{x + 1},{y},{edge}" not in alledges:
                self._expand_edge(x + 1, y, maxx, maxy, edge, plotcoords, alledges)
        elif edge == 'd':
            if f"{x - 1},{y}" in plotcoords and f"{x - 1},{y + 1}" not in plotcoords and f"{x - 1},{y},{edge}" not in alledges:
                self._expand_edge(x - 1, y, maxx, maxy, edge, plotcoords, alledges)
            if f"{x + 1},{y}" in plotcoords and f"{x + 1},{y + 1}" not in plotcoords and f"{x + 1},{y},{edge}" not in alledges:
                self._expand_edge(x + 1, y, maxx, maxy, edge, plotcoords, alledges)


    def _get_price(self, plotcoords, maxx, maxy):
        edges = 0
        alledges = set()
        for c in plotcoords:
            x, y = map(int, c.split(','))

            # left edge: x,y
            # is an edge if:        x - 1, y is not in plot
            # continues up if:      x, y - 1 is in plot and
            #                       x - 1, y - 1 is not in plot
            # continues down if:    x, y + 1 is in plot and
            #                       x - 1, y + 1 is not in plot
            if f"{x - 1},{y}" not in plotcoords and f"{x},{y},l" not in alledges:
                self._expand_edge(x, y, maxx, maxy, 'l', plotcoords, alledges)
                edges += 1
            # right edge: x,y
            # is an edge if:        x + 1, y is not in plot
            # continues up if:      x, y - 1 is in plot and
            #                       x + 1, y - 1 is not in plot
            # continues down if:    x, y + 1 is in plot and
            #                       x + 1, y + 1 is not in plot
            if f"{x + 1},{y}" not in plotcoords and f"{x},{y},r" not in alledges:
                self._expand_edge(x, y, maxx, maxy, 'r', plotcoords, alledges)
                edges += 1
            # upper edge: x,y
            # is an edge if:        x, y - 1 is not in plot
            # continues left if:    x - 1, y is in plot and
            #                       x - 1, y - 1 is not in plot
            # continues right if:   x + 1, y is in plot and
            #                       x + 1, y - 1 is not in plot
            if f"{x},{y - 1}" not in plotcoords and f"{x},{y},u" not in alledges:
                self._expand_edge(x, y, maxx, maxy, 'u', plotcoords, alledges)
                edges += 1
            # lower edge: x,y
            # is an edge if:        x, y + 1 is not in plot
            # continues left if:    x - 1, y is in plot and
            #                       x - 1, y + 1 is not in plot
            # continues right if:   x + 1, y is in plot and
            #                       x + 1, y + 1 is not in plot
            if f"{x},{y + 1}" not in plotcoords and f"{x},{y},d" not in alledges:
                self._expand_edge(x, y, maxx, maxy, 'd', plotcoords, alledges)
                edges += 1
        return edges * len(plotcoords)

    def run(self, garden):
        maxy = len(garden)
        maxx = len(garden[0])
        
        allplotcoords = set()
        price = 0
        for y in range(maxy):
            for x, plant in enumerate(garden[y]):
                if f"{x},{y}" not in allplotcoords:
                    plotcoords = set()
                    self._expand_plot(garden, plant, x, y, maxx, maxy, plotcoords)
                    price += self._get_price(plotcoords, maxx, maxy)
                    allplotcoords.update(plotcoords)

        return price

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec12a().run_specific_tests(sys.argv[1:])
        Dec12b().run_specific_tests(sys.argv[1:])
    else:
        Dec12a().runtests()
        Dec12b().runtests()
