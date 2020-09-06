from utils import writebmp, norm, V3, color
from sphere import Sphere
from math import pi, tan
from materials import lightblue, body, eye, nose, button

'''
    Diana Ximena de León Figueroa
    Carne 18607
    RT1 - Esferas
    Graficas por Computadora
    04 de deptiembre de 2020
'''

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
BLUE = color(60, 80, 125)


class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.scene = []
        self.currentColor = BLUE
        self.clear()

    def clear(self):
        self.pixels = [
            [self.currentColor for x in range(self.width)]
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
    Sphere(V3(0.7, -5.05, -15), 0.15, button),
    Sphere(V3(-0.8, -5.05, -15), 0.15, button),
    Sphere(V3(0.75, -5, -15), 0.3, eye),
    Sphere(V3(-0.75, -5, -15), 0.3, eye),
    Sphere(V3(0, -4.5, -15), 0.4, nose),
    Sphere(V3(-1, -4, -15), 0.2, button),
    Sphere(V3(-0.4, -3.5, -15), 0.2, button),
    Sphere(V3(0.4, -3.5, -15), 0.2, button),
    Sphere(V3(1, -4, -15), 0.2, button),
    Sphere(V3(0, -2, -15), 0.25, button),
    Sphere(V3(0, 0.25, -15), 0.5, button),
    Sphere(V3(0, 3, -15), 0.75, button),
    Sphere(V3(0, -3.5, -12), 1.5, body),
    Sphere(V3(0, -1, -12), 2, body),
    Sphere(V3(0, 2.5, -12), 2.5, body),
    Sphere(V3(0, 0, -11), 5, lightblue),
]
r.render()
r.write()
