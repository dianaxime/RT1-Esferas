from utils import color

'''
    Diana Ximena de León Figueroa
    Carne 18607
    RT1 - Esferas
    Graficas por Computadora
    04 de deptiembre de 2020
'''


class Material(object):
  def __init__(self, diffuse):
    self.diffuse = diffuse


WHITE = color(215, 200, 200)
BONE = color(240, 225, 205)
ORANGE = color(240, 60, 40)
BLACK = color(10, 10, 10)
LIGHTBLUE = color(100, 130, 200)

body = Material(diffuse = BONE)
button = Material(diffuse = BLACK)
eye = Material(diffuse = WHITE)
nose = Material(diffuse = ORANGE)
lightblue = Material(diffuse = LIGHTBLUE)
