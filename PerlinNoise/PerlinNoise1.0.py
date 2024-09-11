import noise
import PIL as pil
import numpy as np
from random import randint

size = (250,250)
scale = 100.0
octaves = 6
persistance = 0.5
lacunarity = 2.0
seed = randint(0,1000)

grid = np.zeros(size)


for i in range(size[0]):
    for j in range(size[1]):
