"""
# Part 1
input = open("sonarsweep.txt", "r")

numIncreases = 0
prevVal = None
for line in input:
    currentVal = int(line)
    if (prevVal != None) and (prevVal < currentVal):
        numIncreases += 1
    prevVal = currentVal

print (numIncreases)
"""


# Part 2
input = open("sonarsweep.txt", "r")

distances = []
numIncreases = 0

# Load all values into a list for easier processing
for line in input:
    distances.append(int(line))

prevWindow = None
for windowSlider in range(len(distances) - 2):
    curWindow = distances[0 + windowSlider] + distances[1 + windowSlider] + distances[2 + windowSlider]
    if (prevWindow != None) and (prevWindow < curWindow):
        numIncreases += 1
    prevWindow = curWindow

print (numIncreases)
