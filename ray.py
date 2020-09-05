from utils import *
from sphere import *
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
        self.current_color = WHITE
        self.clear()

    def clear(self):
        self.pixels = [
            [BLUE for x in range(self.width)]
            for y in range(self.height)
        ]

    def write(self, filename='out.bmp'):
        writebmp(filename, self.width, self.height, self.pixels)

    def display(self, filename='out.bmp'):
        self.render()
        self.write(filename)

    def point(self, x, y, c=None):
        try:
            self.pixels[y][x] = c or self.current_color
        except:
            pass

    def scene_intersect(self, origin, direction):
        for obj in self.scene:
            if obj.ray_intersect(origin, direction):
                return obj.material
        return None

    def cast_ray(self, orig, direction):
        # esta funcion devuelve un color gracias al rayo
        impacted_material = self.scene_intersect(orig, direction)
        if impacted_material:
            return impacted_material.diffuse
        else:
            return BLUE

    """
    def cast_ray(self, orig, direction, sphere):
    if sphere.ray_intersect(orig, direction):
      return color(255, 0, 0)
    else:
      return color(0, 0, 255)
      """

    def render(self):
        alfa = int(pi/2)
        for y in range(self.height):
            for x in range(self.width):
                i = (2*(x + 0.5)/self.width - 1) * \
                    self.width/self.height*tan(alfa/2)
                j = (1 - 2*(y + 0.5)/self.height)*tan(alfa/2)
                direction = norm(V3(i, j, -1))
                self.pixels[y][x] = self.cast_ray(V3(0, 0, 0), direction)

    """
  def basicRender(self):
  #Esto llena la pantalla de un color degradado
    for x in range(self.width):
      for y in range(self.height):
        r = int((x/self.width)*255) if x/self.width < 1 else 1
        g = int((y/self.height)*255) if y/self.height < 1 else 1
        b = 0
        self.pixels[y][x] = color(r, g, b)
        """


r = Raytracer(1000, 1000)
r.scene = [
    Sphere(V3(-0.6, -2.1, -10), 0.1, button),
    Sphere(V3(-0.2, -1.9, -10), 0.1, button),
    Sphere(V3(0.2, -1.9, -10), 0.1, button),
    Sphere(V3(0.6, -2.1, -10), 0.1, button),

    Sphere(V3(0, -2.5, -10), 0.3, carrot),

    Sphere(V3(0.5, -3, -10), 0.1, button),
    Sphere(V3(-0.5, -3, -10), 0.1, button),
    Sphere(V3(0.5, -3, -10), 0.2, eye),
    Sphere(V3(-0.5, -3, -10), 0.2, eye),

    Sphere(V3(0, -0.4, -10), 0.3, button),
    Sphere(V3(0, 1, -10), 0.4, button),
    Sphere(V3(0, 3, -10), 0.5, button),
    Sphere(V3(0, -2.5, -10), 1.3, snow),
    Sphere(V3(0, 0, -10), 1.8, snow),
    Sphere(V3(0, 3, -12), 2.8, snow)
]
r.display()
