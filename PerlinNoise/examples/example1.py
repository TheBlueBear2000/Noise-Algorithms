import noise
import numpy as np
from PIL import Image
from scipy import toImage

shape = (500,500)
scale = .5
octaves = 3
persistence = 0.5
lacunarity = 2.0
seed = np.random.randint(0,100)

world = np.zeros(shape)

# make coordinate grid on [0,1]^2
x_idx = np.linspace(0, 1, shape[0])
y_idx = np.linspace(0, 1, shape[1])
world_x, world_y = np.meshgrid(x_idx, y_idx)

# apply perlin noise, instead of np.vectorize, consider using itertools.starmap()
world = np.vectorize(noise.pnoise2)(world_x/scale,
                        world_y/scale,
                        octaves=octaves,
                        persistence=persistence,
                        lacunarity=lacunarity,
                        repeatx=shape[0],
                        repeaty=shape[1],
                        base=seed)

def colorWorld(world):

    water = [65,105,225]
    land = [34,139,34]
    beach = [238,214,175]
    mountain = [100,100,100]
    snow = [250,250,250]


    coloredWorld = np.zeros(world.shape + (3,))
    for y in range(shape[0]):
        for x in range(shape[1]):
            if world[y][x] < -0.05:
                coloredWorld[y][x] = water
            elif world[y][x] < 0:
                coloredWorld[y][x] = beach
            elif world[y][x] < 0.35:
                coloredWorld[y][x] = land
            elif world[y][x] < 0.55:
                coloredWorld[y][x] = mountain
            elif world[y][x] < 1.0:
                coloredWorld[y][x] = snow
    
    return coloredWorld

#colored_world = colorWorld(world)

# here was the error: one needs to normalize the image first. Could be done without copying the array, though
img = np.floor((world + .5) * 255).astype(np.uint8) # <- Normalize world first
Image.fromarray(img, mode='L').show()

#toImage(colored_world).show()

