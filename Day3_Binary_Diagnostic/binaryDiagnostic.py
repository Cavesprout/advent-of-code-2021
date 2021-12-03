"""

# Part 1
input = open("binaryDiagnostic.txt", "r")

gammaRate = ''
epsilonRate = ''

data = []
for line in input:
    data.append(line.replace('\n', ''))

# For Each Index
for i in range(len(data[0])):
    num0 = 0
    num1 = 1
    # Iterate through each line at that index, tallying the 1s and 0s
    for line in data:
        if (line[i] == '0'):
            num0 += 1
        else:
            num1 += 1
    print (num0)
    print (num1)


    if (num0 < num1):
        gammaRate += '1'
        epsilonRate += '0'
        
    else:
        gammaRate += '0'
        epsilonRate += '1'
    
print(gammaRate)
print(epsilonRate)

gammaRateAsInt = 0
for i in range(len(gammaRate)):
    gammaRateAsInt += int(gammaRate[len(gammaRate) - i - 1]) * (2 ** i)

print(gammaRateAsInt)

epsilonRateAsInt = 0
for i in range(len(gammaRate)):
    epsilonRateAsInt += int(epsilonRate[len(epsilonRate) - i - 1]) * (2 ** i)

print(epsilonRateAsInt)

print(gammaRateAsInt * epsilonRateAsInt)


"""

# Part 2
input = open("binaryDiagnostic.txt", "r")

data = []
for line in input:
    data.append(line.replace('\n', ''))


OxygenValues = data
CO2Values = data

# For Each Index
for i in range(len(data[0])):
    OxyNum0 = 0
    OxyNum1 = 0
    # Iterate through each line at that index, tallying the 1s and 0s
    for line in OxygenValues:
        if (line[i] == '0'):
            OxyNum0 += 1
        else:
            OxyNum1 += 1
    print (OxyNum0)
    print (OxyNum1)

    CO2Num0 = 0
    CO2Num1 = 0
    for line in CO2Values:
        if (line[i] == '0'):
            CO2Num0 += 1
        else:
            CO2Num1 += 1
    print (CO2Num0)
    print (CO2Num1)

    newOxygenValues = []
    if (OxyNum0 > OxyNum1):
        for line in OxygenValues:
            if line[i] == '0':
                newOxygenValues.append(line)
    if (OxyNum1 >= OxyNum0):
        for line in OxygenValues:
            if line[i] == '1':
                newOxygenValues.append(line)
    print("O2: " + str(newOxygenValues))
    OxygenValues = newOxygenValues

    newC02Values = []
    if (CO2Num0 > CO2Num1):
        for line in CO2Values:
            if line[i] == '1':
                newC02Values.append(line)
    if (CO2Num1 >= CO2Num0):
        for line in CO2Values:
            if line[i] == '0':
                newC02Values.append(line)
    print("CO2: " + str(newC02Values))
    CO2Values = newC02Values


    if len(CO2Values) == 1:
        foundCO2Rating = CO2Values[0]
    if len(OxygenValues) == 1:
        foundO2Rating = OxygenValues[0]

print(foundO2Rating)
print(foundCO2Rating)


O2AsInt = 0
for i in range(len(foundO2Rating)):
    O2AsInt += int(foundO2Rating[len(foundO2Rating) - i - 1]) * (2 ** i)

print(O2AsInt)

CO2AsInt = 0
for i in range(len(foundCO2Rating)):
    CO2AsInt += int(foundCO2Rating[len(foundCO2Rating) - i - 1]) * (2 ** i)

print(CO2AsInt)

print(O2AsInt * CO2AsInt)