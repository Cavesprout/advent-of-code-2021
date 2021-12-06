"""
# Part 1

input = open("lanternfish.txt", "r")

activeFish = []
for i in input.readline().split(","):
    activeFish.append(int(i))

for day in range(80):
    for idx, fish in enumerate(activeFish):
        activeFish[idx] -= 1
        if activeFish[idx] == -1:
            activeFish[idx] = 6
            activeFish.append(9)
    print(f"Day {day + 1} has {len(activeFish)} fish")

"""

# Part 2
# Fun fact: exponential running time is bad!

input = open("lanternfish.txt", "r")

activeFish = []
for i in input.readline().split(","):
    activeFish.append(int(i))

fishOfNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for fish in activeFish:
    fishOfNum[fish] += 1

print(fishOfNum)

numDays = 256
for i in range(numDays):
    # Before any operations, find number of new fish spawned
    spawningFish = fishOfNum[0]
    # For fish numbered 1 through 8, simply move down the list
    for i in range(8):
        fishOfNum[i] = fishOfNum[i+1]
    # Spawn new fish and reset spawning fish to position 6
    fishOfNum[8] = spawningFish
    fishOfNum[6] += spawningFish
    

print(fishOfNum)

totalfish = 0
for fishGroup in fishOfNum:
    totalfish += fishGroup

print(totalfish)

# print(f"Day {day + 1} has {len(activeFish)} fish")