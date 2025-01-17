from PIL import Image
from numpy import array
import colorsys
import time

resolution = 10001
d = 2

img = Image.new('RGB', (resolution, resolution), color='white')

def GenerateColour(n):
    colour = 255 * array(colorsys.hsv_to_rgb(n / 255, 1, 0.5))
    return tuple(colour.astype(int))

def CheckComplexNumber(a, b):
    a = a / ((resolution-1)/4) - 2
    b = b / ((resolution-1)/4) - 2
    z = 0
    c = complex(a, b)
    initialAbs = abs(c)
    for i in range(100):
        z = z ** d + c
        if abs(z) > 2: return GenerateColour(i)
    return (0, 0, 0)

def CreateMandelbrotSet():
    loops = 0
    if resolution % 2 != 0:
        resolutionY = (resolution - 1) / 2 + 1
    else:
        resolutionY = resolution / 2 + 1
    for y in range(int(resolutionY)):
        for x in range(resolution):
            colour = CheckComplexNumber(x, y)
            img.putpixel( (x, y), colour)
            img.putpixel( (x, y * -1), colour)
        loops += 1
        percentage = loops / resolutionY * 100
        print(str(round(percentage, 2)) + '%')

startTime = time.perf_counter()
CreateMandelbrotSet()
endTime = time.perf_counter()
timeTaken = endTime - startTime
print(timeTaken)
img.save("Mandelbrot-Set-C-tmp", "png")
img.show()
