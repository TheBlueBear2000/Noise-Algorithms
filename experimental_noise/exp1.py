import math
from PIL import Image

WIDTH, HEIGHT = 500, 500
SEED = 234

def getRand(x, max, min = 0):
    if x == 0:
        x = 3456
    x = abs((x*(55+x) * 22.5) / (x/2) * (x*5))/(56*x)+41267.3269874/583*x
    x = (x - int(x)) * (max-min) + min
    return int(x)


def myPerlin(loc, seed):
    findX = loc[0]
    findY = loc[1]
    vals = []
    i = 0
    total = 0
    
    for y in range(int(findY)-1, int(findY) + 2):
        vals.append([])
        for x in range(int(findX)-1, int(findX) + 2):
            numX = getRand(x, 256)
            numY = getRand(y, 256)
            val = (numX + numY) // 2
            dist = abs(math.sqrt(((findX - x) ** 2)  +  ((findY - y) ** 2)))
            total += dist * val
        i += 1
        
    return int(total)


im = Image.new('RGBA', (WIDTH, HEIGHT), (255, 255, 255, 255))

for y in range(HEIGHT):
    for x in range(WIDTH):
        val = myPerlin((x, y), SEED)
        im.paste(Image.new('RGBA', (1,1), (val, val, val, 255)), (x,y))
    
im.save("outputs/exp_noise1/out.png")
print("done!")
            
            