#Create a function that takes the volume of a cube and returns the length of the cube's main diagonal, rounded to two decimal places.
import math

def cube_diagonal(volume):
    diagonal = math.pow((6 * volume / math.pi), 1/3)
    rounded_diagonal = round(diagonal, 2)
    return rounded_diagonal

print(cube_diagonal(8))         
