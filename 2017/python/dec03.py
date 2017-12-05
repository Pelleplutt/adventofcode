import task
import math

# 65 64 63  62  61  60  59 58 57
# 66 37 36  35  34  33  32 31 56
# 67 38 17  16  15  14  13 30 55
# 68 39 18   5   4   3  12 29 54
# 69 40 19   6   1   2  11 28 53
# 70 41 20   7   8   9  10 27 52
# 71 42 21  22  23  24  25 26 51
# 72 43 44  45  46  47  48 49 50
# 73 74 75  76  77  78  79 80 81 

class dec03_1(task.task):
    """
    You come across an experimental new kind of memory stored on an infinite
    two-dimensional grid.

    Each square on the grid is allocated in a spiral pattern starting at a
    location marked 1 and then counting up while spiraling outward. For
    example, the first few squares are allocated like this:

        17  16  15  14  13
        18   5   4   3  12
        19   6   1   2  11
        20   7   8   9  10
        21  22  23---> ...
        While this is very space-efficient (no squares are skipped), requested
        data must be carried back to square 1 (the location of the only access
        port for this memory system) by programs that can only move up, down,
        left, or right. They always take the shortest path: the Manhattan
        Distance between the location of the data and square 1.

        For example:

            Data from square 1 is carried 0 steps, since it's at the access port.
            Data from square 12 is carried 3 steps, such as: down, left, left.
            Data from square 23 is carried only 2 steps: up twice.
            Data from square 1024 must be carried 31 steps.
            How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?
    """
    def init(self):
        self.in_int = True

    def run(self, data):
        gridsize = int(math.sqrt(data))
        # Size is always odd as we increment by two from one
        if gridsize * gridsize < data:
            gridsize = gridsize + 1
        if gridsize % 2 == 0:
            gridsize = gridsize + 1

        gridmax = gridsize * gridsize

        # the start will always be on the outer edge, we always need to go this
        # many steps
        steps = int(gridsize / 2)

        # where is the number, calculate the edge by subtracting number from
        # max and dividing by edge size rounding upwards. Last edge numberwise
        # (bottom) will be 0, left will be 1, top be 2, right be 3
        #edge = math.ceil((gridmax - data) / gridsize)
        if gridsize > 1:
            edge = int((gridmax - data) / (gridsize - 1))
        else:
            edge = 0

        # calculate the middle number of that edge, offset to this number will
        # control how many steps we need to take to get to center
        edgepivot = gridmax - edge * (gridsize - 1) - int(gridsize / 2)

        # now offset out number to the edge pivot
        steps = steps + abs(edgepivot - data)

        # tada.wav
        return steps

class dec03_2(task.task):
    """
    As a stress test on the system, the programs here clear the grid and then
    store the value 1 in square 1. Then, in the same allocation order as shown
    above, they store the sum of the values in all adjacent squares, including
    diagonals.

    So, the first few squares' values are chosen as follows:

        Square 1 starts with the value 1.
        Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
        Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
        Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
        Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
        Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

            147  142  133  122   59
            304    5    4    2   57
            330   10    1    1   54
            351   11   23   25   26
            362  747  806--->   ...
            What is the first value written that is larger than your puzzle input?
    """
    def init(self):
        self.in_int = True

    def getedgevalues(self, gridsize, edge):
        if gridsize == 1:
            return [1]
        gridmax = gridsize * gridsize
        edgemax = gridmax - edge * (gridsize - 1)
        edgemin = gridmax - (edge + 1) * (gridsize - 1)

        # Reverse it as we are always going from high to low
        return list(reversed(range(edgemin + 1, edgemax + 1)))

    def getlowerorderneighbours(self, home):
        # special case
        if home == 1:
            return []

        neighbours = []

        # Perform the basic calculations from dec03_1 to find our edge and offset
        # in the matrix
        gridsize = int(math.sqrt(home))

        if gridsize * gridsize < home:
            gridsize = gridsize + 1
        if gridsize % 2 == 0:
            gridsize = gridsize + 1

        gridmax = gridsize * gridsize

        if gridsize > 1:
            edge = int((gridmax - home) / (gridsize - 1))
        else:
            edge = 0

        # If we are not first, our immediate lower will always neighbour us
        neighbours.append(home - 1)

        # calculate the size and contents of the immediate inner grid from us
        innergridsize = gridsize - 2

        inneredges = []
        ouredges = []

        for genedge in range(4):
            inneredges.append(self.getedgevalues(innergridsize, genedge))
            ouredges.append(self.getedgevalues(gridsize, genedge))

        # corneroffset is position relative to the corner, offset 0 means we are in a corner,
        # -1 means we are on the "higher number side" of the corner, +1 on the lower side
        corneroffset = (gridmax - home) % (gridsize - 1)

        if corneroffset == 0:
            # Are we a "corner number", if so we will only neighbour one
            # additional other, i.e. the corner in the inner ring and
            # possibly the first number on this grid

            # Edge 0 corner, add the first number in our gridsize
            if edge == 0 and home > 1:
                neighbours.append(ouredges[3][-1])

            # Add the corner number from the corner in the inner grid
            innercornervalue = inneredges[edge][0]
            neighbours.append(innercornervalue)

        if corneroffset == 1:
            # Are next to a corner on the lower side?, if so we will neighbour the inner
            # corner and the square at our relative position to the corner

            # add neighbour in our corner
            innercornervalue = inneredges[edge][0]
            neighbours.append(innercornervalue)

            # Add the immediate next to in the inner ring
            if len(inneredges[edge]) > 1:
                nexttoinnercornervalue = inneredges[edge][1]
                neighbours.append(nexttoinnercornervalue)

            # Edge 0 corner, add the first number in our gridsize
            if edge == 0 and home > 1:
                neighbours.append(ouredges[3][-1])
        if corneroffset == (gridsize - 2):
            # Are next to a corner on the higher side? We will border our
            # home -2 (unless we are on the 3rd edge), the immediate corner
            # on the inside and the number on our correspodning offset to
            # that corner

            # Add cross corner to the lower integer side
            if edge < 3:
                neighbours.append(home - 2)

            # Add immediate next to neighbour
            if len(inneredges[edge]) > 1:
                innernexttoadd = inneredges[edge][-1]
                neighbours.append(innernexttoadd)

            # Corner cases for the rest of edges as we need to peek into the
            # neighbouring edges for the bordering
            if edge == 2 and len(inneredges[edge]) > 1:
                nexttoinnercornervalue = inneredges[3][0]
                neighbours.append(nexttoinnercornervalue)
            elif edge == 1 and len(inneredges[edge]) > 1:
                nexttoinnercornervalue = inneredges[2][0]
                neighbours.append(nexttoinnercornervalue)
            elif edge == 0 and len(inneredges[edge]) > 1:
                nexttoinnercornervalue = inneredges[1][0]
                neighbours.append(nexttoinnercornervalue)

        if corneroffset > 1 and corneroffset < (gridsize - 2):
            # Are we not in a corner not next to it? we will neighbour 3
            # additional ones, the one directly inner to us and its two
            # neighbours

            # we will neighbour our corresponding number on the inner circle,
            # which is our corneroffset - 1 and then it's immediate neighbours,
            # so +1 and -1 respecivly
            cornerhigh = gridmax - edge * (gridsize - 1)
            cornerhighoffset = cornerhigh - home

            offset = cornerhighoffset - 1

            # Make sure to cater for wrapping to neighbouring edge
            neighbours.append(inneredges[edge][offset - 1])
            neighbours.append(inneredges[edge][offset])
            if offset + 1 == len(inneredges[edge]):
                neighbours.append(inneredges[(edge + 1) % 4][0])
            else:
                neighbours.append(inneredges[edge][offset + 1])

        return sorted(list(set(neighbours)))

    def test_getlowerorderneighbours(self):
        facit = {
            1: [],
            2: [1],
            3: [1, 2],
            4: [1, 2, 3],
            5: [1, 4],
            6: [1, 4, 5],
            7: [1, 6],
            8: [1, 2, 6, 7],
            9: [1, 2, 8],
            10: [2, 9],
            11: [2, 3, 9, 10],
            12: [2, 3, 11],
            13: [3, 12],
            14: [3, 4, 12, 13],
            15: [3, 4, 5, 14],
            16: [4, 5, 15],
            17: [5, 16],
            18: [5, 6, 16, 17],
            19: [5, 6, 7, 18],
            20: [6, 7, 19],
            21: [7, 20],
            22: [7, 8, 20, 21],
            23: [7, 8, 9, 22],
            24: [8, 9, 10, 23],
            25: [9, 10, 24],
            26: [10, 25],
            27: [10, 11, 25, 26],
            28: [10, 11, 12, 27],
            29: [11, 12, 13, 28],
            30: [12, 13, 29],
            31: [13, 30],
            32: [13, 14, 30, 31],
            33: [13, 14, 15, 32],
            34: [14, 15, 16, 33],
            35: [15, 16, 17, 34],
            36: [16, 17, 35],
            37: [17, 36],
            38: [17, 18, 36, 37],
            39: [17, 18, 19, 38],
            41: [19, 20, 21, 40],
            42: [20, 21, 41],
            43: [21, 42],
            44: [21, 22, 42, 43],
            45: [21, 22, 23, 44],
            46: [22, 23, 24, 45],
            47: [23, 24, 25, 46],
            48: [24, 25, 26, 47],
            49: [25, 26, 48],
        }

        notok = []
        for offset, val in facit.items():
            result = self.getlowerorderneighbours(offset)
            print("{0} -> {1}: ".format(offset, result), end='')
            if result == val:
                print("OK")
            else:
                print("NOT OK, expected {0}", val)
                notok.append(offset)

        print(notok)

    def run(self, data):
        # we go from lower to higher, so only need to check the numbers we have
        # already done, store the done numbers in the correct offset in this
        # array
        cellsfilled = [0]

        cell = 0
        while True:
            cell = cell + 1
            neighbours = self.getlowerorderneighbours(cell)
            if cell == 1:
                cellsum = 1
            else:
                cellsum = 0

            for neighbour in neighbours:
                cellsum = cellsum + cellsfilled[neighbour]

            if cellsum > data:
                return cellsum

            cellsfilled.append(cellsum)

if __name__ == "__main__":
    dec03_1().runtests()
    dec03_2().runtests()
