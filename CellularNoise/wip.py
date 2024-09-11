import random
import math
from PIL import Image 


random.seed(int(input("Please enter the seed:  ")))


grid = []

trueStatements = ["YES", "YES PLEASE", "YEAH", "TRUE", "YE", "YE YE YE", "OK", "MHM", "SURE", "POSITIVE", "Y", "1"]
falseStatements = ["NO", "NO THANKS", "NOPE", "FALSE", "NAH", "NEGATIVE", "N", "0"]

while True:
    width = int(input("Please enter the grid width:  "))
    if width > 0:
        break
    print("Please enter a positive interger")

while True:
    height = int(input("Please enter the grid height:  "))
    if height > 0:
        break
    print("Please enter a positive interger")

while True:
    pointDistance = int(input("Please enter the average point distance:  "))
    if pointDistance > 0:
        break
    print("Please enter a positive interger")


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
    while True:
        formatBiomes = input("Would you like the biomes to have a neat color pallette:  ")
        if formatBiomes.upper() in trueStatements:
            formatBiomes = True
            break
        elif formatBiomes.upper() in falseStatements:
            formatBiomes = False
            break
        else:
            print("Invalid entry. Please enter Yes or No")
    
    if formatBiomes:
        while True:
            colourRange = input("Please enter the colour range (as a persentage):  ")
            if colourRange.endswith("%"):
                colourRange = colourRange[:-1]
            colourRange = int(colourRange)
            if 0 < colourRange <= 100:
                colourRange = 255 / 100 * colourRange
                break
            print("Please enter a number between 1 and 100")
    while True:
        overlayMap = input("Would you like to overlay a height map aswell:  ")
        if overlayMap.upper() in trueStatements:
            overlayMap = True
            break
        elif overlayMap.upper() in falseStatements:
            overlayMap = False
            break
        else:
            print("Invalid entry. Please enter Yes or No")
    
        


print("Processing inputs...")

if haveBiomes:
    biomeColors = []
    if formatBiomes:
        averageColor = (int(random.random() * (255-colourRange)),int(random.random() * (255-colourRange)),int(random.random() * (255-colourRange)))
        averageInvertedColor = (255 - averageColor[0], 255 - averageColor[1], 255 - averageColor[2])
    for biome in range(biomeNumber):
        while True:
            if formatBiomes:
                if random.random() > 0.5:
                    biomeColor = (int(random.random()*colourRange) + averageColor[0],int(random.random()*colourRange) + averageColor[1],int(random.random()*colourRange) + averageColor[2],255)
                else:
                    biomeColor = (int(random.random()*colourRange) + averageInvertedColor[0],int(random.random()*colourRange) + averageInvertedColor[1],int(random.random()*colourRange) + averageInvertedColor[2],255)
            else:
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
            if overlayMap:
                image.paste(Image.new('RGBA', (1,1), (int(distances[0][1][0][0]), int(distances[0][1][0][1]), int(distances[0][1][0][2]), int(grid[y][x][0]*255/pointDistance) if grid[y][x][0] < pointDistance else 255)), (x,y))
            else:
                image.paste(Image.new('RGBA', (1,1), (int(distances[0][1][0][0]), int(distances[0][1][0][1]), int(distances[0][1][0][2]), 255)), (x,y))

        # If there are not biomes
        else:
            for point in points:
                value = math.sqrt(((point[0] - x) ** 2) + ((point[1] - y) ** 2))
                distances.append(value)
            #print(distances)
            grid[y][x] = min(distances)
            pixelIntencity = int(min(distances)*255/pointDistance) if min(distances) < pointDistance else 255
            image.paste(Image.new('RGBA', (1,1), (pixelIntencity, pixelIntencity, pixelIntencity, 255)), (x,y))



# Print Grid #

rawgradient = ["#","+","=","-"," "]
#rawgradient = [" "," ","#"," "," "]
rawgradient.reverse()
steepness = 50
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

image.save("CellularNoise.png")

#for row in grid:
#    print(row)

print("Finished!")