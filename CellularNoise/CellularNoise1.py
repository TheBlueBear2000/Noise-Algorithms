import random
import math
from PIL import Image

random.seed(int(input("Please enter the seed:  ")))
#print(random.random())

grid = []

trueStatements = ["YES", "YES PLEASE", "YEAH", "TRUE", "YE", "YE YE YE", "OK", "MHM", "SURE", "POSITIVE", "Y", "1"]
falseStatements = ["NO", "NO THANKS", "NOPE", "FALSE", "NAH", "NEGATIVE", "N", "0"]

width, height = int(input("Please enter the grid width:  ")), int(input("Please enter the grid height:  "))
pointDistance = int(input("Please enter the average point distance:  "))

while True:
    haveBiomes = input("Would you like to have biomes:  ")

    if haveBiomes.upper() in trueStatements:
        haveBiomes = True
        break
    elif haveBiomes.upper() in falseStatements:
        haveBiomes = False
        break
    else:
        print("Invalid entry. Please enter Yes or No")

if haveBiomes:
    biomeNumber = int(input("Please enter the number of biomes:  "))


print("Processing inputs...")

if haveBiomes:
    biomeColors = []
    for biome in range(biomeNumber):
        while True:
            biomeColor = (int(random.random()*255),int(random.random()*255),int(random.random()*255),255)
            if not biomeColor in biomeColors:
                break
        biomeColors.append(biomeColor)

image = Image.new('RGBA', (width, height), (255, 255, 255, 255))


# Generate grid #

for y in range(height):
    row = []
    for x in range(width):
        row.append(0)
    grid.append(row)


# Select points #

print("Locating Peaks...")

points = []

for y in range(int(len(grid)/ pointDistance)):
    for x in range(int(len(grid[y])/ pointDistance)):
        points.append((int(random.random() * pointDistance) + (x * pointDistance) , int(random.random() * pointDistance) + (y * pointDistance) , (biomeColors[int(random.random() * biomeNumber)],biomeColors[int(random.random() * biomeNumber)],biomeColors[int(random.random() * biomeNumber)])) if haveBiomes else (int(random.random() * pointDistance) + (x * pointDistance) , int(random.random() * pointDistance) + (y * pointDistance)))



# Calculate Grid #

print("Running calculations...")

for y in range(len(grid)):
    print("Row {} out of {}...".format(y,len(grid)))
    for x in range(len(row)):
        distances = []
        # If there are biomes
        if haveBiomes:
            for point in points:
                value = math.sqrt(((point[0] - x) ** 2) + ((point[1] - y) ** 2))
                distances.append([value,point[2]])
            distances.sort()
            grid[y][x] = distances[0]
            image.paste(Image.new('RGBA', (1,1), (int(distances[0][1][0][0]), int(distances[0][1][0][1]), int(distances[0][1][0][2]), 255)), (x,y))

        # If there are not biomes
        else:
            for point in points:
                value = math.sqrt(((point[0] - x) ** 2) + ((point[1] - y) ** 2))
                distances.append(value)
            #print(distances)
            grid[y][x] = min(distances)
            pixelIntencity = int(min(distances)*25.5) if min(distances) < 10 else 255
            image.paste(Image.new('RGBA', (1,1), (pixelIntencity, pixelIntencity, pixelIntencity, 255)), (x,y))



# Print Grid #

rawgradient = ["#","+","=","-"," "]
#rawgradient = [" "," ","#"," "," "]
rawgradient.reverse()
steepness = 2
gradient = []
for char in rawgradient:
    for i in range(steepness):
        gradient.append(char)

for row in grid:
    string = ""
    for x in row:
        if haveBiomes:
            string += gradient[len(gradient)-1] if x[0] > len(gradient) - 1 else gradient[int(x[0])]
        else:
            string += gradient[len(gradient)-1] if x > len(gradient) - 1 else gradient[int(x)]
    print(string)

image.save("WORKINGoutput.png")

print("Finished!")