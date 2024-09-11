
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
        



img = np.floor((world + .5) * 255).astype(np.uint8) # <- Normalize world first

#print(img.tolist())
Image.fromarray(img, mode='L').save("out3.png")