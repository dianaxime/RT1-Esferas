from utils import *
from sphere import Sphere
from math import pi, tan
from materials import *

'''
    Diana Ximena de León Figueroa
    Carne 18607
    RT1 - Esferas
    Graficas por Computadora
    04 de deptiembre de 2020
'''

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
BLUE = color(0, 49, 82)


class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.scene = []
        self.currentColor = BLACK
        self.clear()

    def clear(self):
        self.pixels = [
            [BLACK for x in range(self.width)]
            for y in range(self.height)
        ]

    def write(self, filename='out.bmp'):
        writebmp(filename, self.width, self.height, self.pixels)

    def point(self, x, y, selectColor=None):
        try:
            self.pixels[y][x] = selectColor or self.currentColor
        except:
            pass

    def sceneIntersect(self, origin, direction):
        for obj in self.scene:
            if obj.rayIntersect(origin, direction):
                return obj.material
        return None

    def castRay(self, origin, direction):
        # esta funcion devuelve un color gracias al rayo
        impactedMaterial = self.sceneIntersect(origin, direction)
        if impactedMaterial:
            return impactedMaterial.diffuse
        else:
            return self.currentColor

    def render(self):
        fov = int(pi / 2) # field of view
        for y in range(self.height):
            for x in range(self.width):
                i = (2 * (x + 0.5) / self.width - 1) * self.width / self.height * tan(fov / 2)
                j = (1 - 2 * (y + 0.5) / self.height) * tan(fov / 2)
                direction = norm(V3(i, j, -1))
                self.pixels[y][x] = self.castRay(V3(0, 0, 0), direction)


    def gradientBackground(self):
        for x in range(self.width):
            for y in range(self.height):
                r = int((x / self.width) * 255) if x / self.width < 1 else 1
                g = int((y / self.height) * 255) if y / self.height < 1 else 1
                b = 0
                self.pixels[y][x] = color(r, g, b)
    


r = Raytracer(1000, 1000)
r.scene = [
    Sphere(V3(0, -1.5, -10), 1.5, ivory),
    Sphere(V3(0, -1, -12), 2, snow),
]
r.render()
r.write()
