from PIL import Image
from numpy import array
import colorsys

resolution = 10001

img = Image.new('RGB', (resolution, resolution), color='white')

def GenerateColour(n):
    colour = 255 * array(colorsys.hsv_to_rgb(n / 255, 1, 0.5))
    return tuple(colour.astype(int))

def CheckComplexNumber(a, b):
    a = a / ((resolution-1)/4) - 2
    b = b / ((resolution-1)/4) - 2
    z = 0
    n = 0
    c = complex(a, b)
    initialAbs = abs(c)
    for i in range(100):
        z = z * z + c
        n += 1
        if abs(z) > 2: return GenerateColour(n)
    return (0, 0, 0)

def CreateMandelbrotSet():
    loops = 0
    for y in range(resolution):
        for x in range(resolution):
            colour = CheckComplexNumber(x, y)
            img.putpixel( (x, y), colour)
            loops += 1
            print(str(loops / resolution ** 2 * 100) + '%')

CreateMandelbrotSet()
img.save("Mandelbrot-Set-C-tmp", "png")
img.show()
