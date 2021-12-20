#!/usr/bin/env python3

import sys
import task

def getpixel(image, infinitepixel, x, y):
    if x < 0 or x >= len(image[0]):
        return infinitepixel
    if y < 0 or y >= len(image):
        return infinitepixel

    return image[y][x]

def enhance(image, pixels, infinitepixel):
    newimage = []
    for y in range(-2, len(image) + 2):
        newimagerow = ''
        for x in range(-2, len(image[0]) + 2):
            imagestr = getpixel(image, infinitepixel, x - 1, y - 1) +\
                       getpixel(image, infinitepixel, x,     y - 1) +\
                       getpixel(image, infinitepixel, x + 1, y - 1) +\
                       getpixel(image, infinitepixel, x - 1, y) +\
                       getpixel(image, infinitepixel, x,     y) +\
                       getpixel(image, infinitepixel, x + 1, y) +\
                       getpixel(image, infinitepixel, x - 1, y + 1) +\
                       getpixel(image, infinitepixel, x,     y + 1) +\
                       getpixel(image, infinitepixel, x + 1, y + 1)
            index = int(imagestr.replace('.', '0').replace('#', '1'), 2)
            newimagerow += pixels[index]
        newimage.append(newimagerow)
    if infinitepixel == '.':
        infinitepixel = pixels[0]
    else:
        infinitepixel = pixels[-1]
    return newimage, infinitepixel


class Dec20a(task.StrTask):
    """
    """
    def run_list(self, data):
        pixels = data[0]
        image = data[2:]

        infinitepixel = '.'
        image, infinitepixel = enhance(image, pixels, infinitepixel)
        image, infinitepixel = enhance(image, pixels, infinitepixel)

        count = sum([len(list(filter(lambda x: x == '#', row))) for row in image])
        return count

class Dec20b(task.StrTask):
    """
    """
    def run_list(self, data):
        pixels = data[0]
        image = data[2:]

        infinitepixel = '.'
        for i in range(50):
            image, infinitepixel = enhance(image, pixels, infinitepixel)

        count = sum([len(list(filter(lambda x: x == '#', row))) for row in image])

        return count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec20a().run_tests_from_commandline()
        Dec20b().run_tests_from_commandline()
    else:
        Dec20a().runtests()
        Dec20b().runtests()
