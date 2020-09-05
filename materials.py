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


IVORY = color(100, 100, 80)
RUBBER = color(80, 10, 0)
SNOW = color(222, 231, 236)
BLACK = color(0, 0, 0)
WHITE = color(250, 250, 250)
ORANGE = color(255, 165, 0)

ivory = Material(diffuse=IVORY)
rubber = Material(diffuse=RUBBER)
snow = Material(diffuse=SNOW)
button = Material(diffuse=BLACK)
eye = Material(diffuse=WHITE)
carrot = Material(diffuse=ORANGE)