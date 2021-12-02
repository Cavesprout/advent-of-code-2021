"""
# Part 1

input = open("dive.txt", "r")

steps = []
for line in input:
    lineText = line.replace('\n',"")
    if lineText[0] == 'f':
        lineText = lineText.replace("forward ", "")
        step = ("forward", int(lineText))
    if lineText[0] == 'u':
        lineText = lineText.replace("up ", "")
        step = ("up", int(lineText))
    if lineText[0] == 'd':
        lineText = lineText.replace("down ", "")
        step = ("down", int(lineText))
    steps.append(step)
print(steps)

horizpos = 0
depthpos = 0

for step in steps:
    if step[0] == 'forward':
        horizpos += step[1]
    if step[0] == 'up':
        depthpos -= step[1]
    if step[0] == 'down':
        depthpos += step[1]

print(f"horizpos: {horizpos}")
print(f"depthpos: {depthpos}")

print(horizpos * depthpos)
"""

# Part 2

input = open("dive.txt", "r")

steps = []
for line in input:
    lineText = line.replace('\n',"")
    if lineText[0] == 'f':
        lineText = lineText.replace("forward ", "")
        step = ("forward", int(lineText))
    if lineText[0] == 'u':
        lineText = lineText.replace("up ", "")
        step = ("up", int(lineText))
    if lineText[0] == 'd':
        lineText = lineText.replace("down ", "")
        step = ("down", int(lineText))
    steps.append(step)
print(steps)

horizpos = 0
depthpos = 0
aim = 0

for step in steps:
    if step[0] == 'forward':
        horizpos += step[1]
        depthpos += aim * step[1]
    if step[0] == 'up':
        aim -= step[1]
    if step[0] == 'down':
        aim += step[1]

print(f"horizpos: {horizpos}")
print(f"depthpos: {depthpos}")

print(horizpos * depthpos)