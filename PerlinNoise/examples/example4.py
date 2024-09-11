
import noise
import numpy as np
from PIL import Image

shape = (500,500)
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0
seed = 10

world = np.zeros(shape)

# make coordinate grid on [0,1]^2
x_idx = np.linspace(0, 1, shape[0])
y_idx = np.linspace(0, 1, shape[1])
world_x, world_y = np.meshgrid(x_idx, y_idx)


for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=shape[0], 
                                    repeaty=shape[1], 
                                    base=0)
        
def colorWorld(world):
    
    water = [65,105,225]
    land = [34,139,34]
    beach = [238,214,175]
    mountain = [100,100,110]
    snow = [250,250,255]


    coloredWorld = np.zeros(world.shape + (3,))
    for y in range(shape[0]):
        for x in range(shape[1]):
            if world[y][x] < 0.3 * 255:
                coloredWorld[y][x] = water
            elif world[y][x] < 0.325 * 255:
                coloredWorld[y][x] = beach
            elif world[y][x] < 0.8 * 255:
                coloredWorld[y][x] = land
            elif world[y][x] < 0.9 * 255:
                coloredWorld[y][x] = mountain
            elif world[y][x] < 1.0 * 255:
                coloredWorld[y][x] = snow
    
    return coloredWorld


img = np.floor((world + .5) * 255).astype(np.uint8) # <- Normalize world first

#print(img.tolist())
Image.fromarray(img, mode='RGB').save("out4.png")