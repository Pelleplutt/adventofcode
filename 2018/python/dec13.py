import task

class Cart(object):
    dirchars = '^>v<'

    def __init__(self, x, y, dirchar):
        self.x = x
        self.y = y
        self.dir = self.dirchars.index(dirchar)
        self.idir = 0
        pass

    def dirchar(self):
        return self.dirchars[self.dir]

    def move(self, field):
        if self.dir == 0:
            self.y -= 1
            if field[self.y][self.x] == '/':
                self.dir = 1
            elif field[self.y][self.x] == '\\':
                self.dir = 3
            elif field[self.y][self.x] == '+':
                self.dir = (3 + self.idir) % 4
                self.idir = (self.idir + 1) % 3
        elif self.dir == 1:
            self.x += 1
            if field[self.y][self.x] == '/':
                self.dir = 0
            elif field[self.y][self.x] == '\\':
                self.dir = 2
            elif field[self.y][self.x] == '+':
                self.dir = (0 + self.idir) % 4
                self.idir = (self.idir + 1) % 3
        elif self.dir == 2:
            self.y += 1
            if field[self.y][self.x] == '/':
                self.dir = 3
            elif field[self.y][self.x] == '\\':
                self.dir = 1
            elif field[self.y][self.x] == '+':
                self.dir = (1 + self.idir) % 4
                self.idir = (self.idir + 1) % 3
        elif self.dir == 3:
            self.x -= 1
            if field[self.y][self.x] == '/':
                self.dir = 2
            elif field[self.y][self.x] == '\\':
                self.dir = 0
            elif field[self.y][self.x] == '+':
                self.dir = (2 + self.idir) % 4
                self.idir = (self.idir + 1) % 3

class Field(object):

    def __init__(self, data):
        self.carts = []
        self.field = []

        for y in range(len(data)):
            s = ''
            for x in range(len(data[y])):
                cart = None
                c = data[y][x]
                if c in Cart.dirchars:
                    cart = Cart(x, y, c)
                    if cart.dir == 0 or cart.dir == 2:
                        c = '|'
                    else:
                        c = '-'
                if cart is not None:
                    self.carts.append(cart)
                s += c
            self.field.append(s)

    def print(self):
        f2 = []
        for row in self.field:
            f2.append(list(row))

        for c in self.carts:
            f2[c.y][c.x] = c.dirchar()

        for row in f2:
            print(''.join(row))


class dec13_1(task.StrTask):
        
    def run_list(self, data):
        field = Field(data)
        
        while True:
            field.carts.sort(key=lambda c: (c.y, c.x))
            for ci1 in range(len(field.carts)):
                field.carts[ci1].move(field.field)

                for ci2 in range(len(field.carts)):
                    if field.carts[ci2].y > field.carts[ci1].y:
                        break

                    if ci1 == ci2:
                        continue

                    if field.carts[ci1].y == field.carts[ci2].y and field.carts[ci1].x == field.carts[ci2].x:
                        return '{},{}'.format(field.carts[ci1].x, field.carts[ci1].y)
        return None

class dec13_2(task.StrTask):
        
    def run_list(self, data):
        field = Field(data)
        
        while True:
            field.carts = list(filter(lambda x: x is not None, field.carts))
            field.carts.sort(key=lambda c: (c.y, c.x))
            if len(field.carts) == 1:
                return '{},{}'.format(field.carts[0].x, field.carts[0].y)

            for ci1 in range(len(field.carts)):
                if field.carts[ci1] is None:
                    continue

                field.carts[ci1].move(field.field)

                for ci2 in range(len(field.carts)):
                    if field.carts[ci2] is None:
                        continue
                    
                    if field.carts[ci2].y > field.carts[ci1].y:
                        break

                    if ci1 == ci2:
                        continue

                    if field.carts[ci1].y == field.carts[ci2].y and field.carts[ci1].x == field.carts[ci2].x:
                        field.carts[ci1] = None
                        field.carts[ci2] = None

                        break
        return None

if __name__ == "__main__":
    dec13_1().runtests()
    dec13_2().runtests()
