# Note to self: Try making an implementation of this one later with a map instead of a massive array representing the entire 2D space!
# You could use the practice! Would probably increase the efficiency quite a lot.

# Also since I swapped the x and y coordinate mid-way through, if I ever reference this code again note that a lot of the print statements are pretty jank.


"""
# Part 1

import numpy as np

input = open("hydrothermalventure.txt", "r")


lineSegments = []

maxX = 0
maxY = 0
# Read Input into List
for line in input:
    x1,y1,x2,y2 = line.replace(" -> ",",").replace("\n", "").split(",")
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    lineSegments.append((x1,y1,x2,y2))
    if x1 > maxX:
        maxX = x1
    if x2 > maxX:
        maxX = x1
    if y1 > maxY:
        maxY = y1
    if y2 > maxY:
        maxY = y2

# Create vent grid
ventMap = np.zeros((maxX+1, maxY+1))


for x1,y1,x2,y2 in lineSegments:
    if (abs(y1 - y2) + 1) == 1 or (abs(x1 - x2) + 1) == 1:
        print(f"Printing Line Segment from ({x1},{y1}) to ({x2},{y2}) for a total of {abs(y1 - y2) + 1} points vertically and {abs(x1 - x2) + 1} points horizontally")
        for i in range(abs(x1 - x2) + 1):
            for j in range(abs(y1 - y2) + 1):
                print(f"Printing Point At ({max(x1, x2) - i},{max(y1, y2) - j})")
                ventMap[max(x1, x2) - i][max(y1, y2) - j] += 1
                

numOverlaps = 0
for i in ventMap:
    for j in i:
        if j > 1:
            numOverlaps += 1



print(ventMap)
print(maxX,maxY)
print(lineSegments)
print(numOverlaps)
"""

# Part 2

import numpy as np

input = open("hydrothermalventure.txt", "r")


lineSegments = []

maxX = 0
maxY = 0
# Read Input into List
for line in input:
    x1,y1,x2,y2 = line.replace(" -> ",",").replace("\n", "").split(",")
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    lineSegments.append((x1,y1,x2,y2))
    if x1 > maxX:
        maxX = x1
    if x2 > maxX:
        maxX = x1
    if y1 > maxY:
        maxY = y1
    if y2 > maxY:
        maxY = y2

# Create vent grid
ventMap = np.zeros((maxY+1, maxX+1))


for x1,y1,x2,y2 in lineSegments:
    print(f"Printing Line Segment from ({x1},{y1}) to ({x2},{y2}) for a total of {abs(y1 - y2) + 1} points vertically and {abs(x1 - x2) + 1} points horizontally")
    # If horizontal or vertical
    if x1 == x2 or y1 == y2:
        for i in range(abs(x1 - x2) + 1):
            for j in range(abs(y1 - y2) + 1):
                print(f"Printing Point At ({max(y1, y2) - i},{max(x1, x2) - j})")
                ventMap[max(y1, y2) - j][max(x1, x2) - i] += 1
    # If diagonal
    else:
        for i in range(abs(x1 - x2) + 1):
            if (y1 > y2) and (x1 > x2):
                print(f"Printing Point At ({max(y1, y2) - i},{max(x1, x2) - j})")
                ventMap[y1 - i][x1 - i] += 1
            if (y1 < y2) and (x1 > x2):
                print(f"Printing Point At ({max(y1, y2) - i},{max(x1, x2) - j})")
                ventMap[y1 + i][x1 - i] += 1
            if (y1 > y2) and (x1 < x2):
                print(f"Printing Point At ({max(y1, y2) - i},{max(x1, x2) - j})")
                ventMap[y1 - i][x1 + i] += 1
            if (y1 < y2) and (x1 < x2):
                print(f"Printing Point At ({max(y1, y2) - i},{max(x1, x2) - j})")
                ventMap[y1 + i][x1 + i] += 1



numOverlaps = 0
for i in ventMap:
    for j in i:
        if j > 1:
            numOverlaps += 1



print(ventMap)
print(maxX,maxY)
print(lineSegments)
print(numOverlaps)
