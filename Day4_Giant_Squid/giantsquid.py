# GOSH DANGIT I FORGOT ENUMERATE EXISTED


# Part 1

from abc import abstractproperty


input = open("giantsquid.txt", "r")
firstLine = input.readline().split(',')

data = []
for line in input:
    dataLine = line.replace('\n', '')
    if (dataLine != ''):
        data.append(dataLine.split())
data.append("END")
boardsAlreadyWon = []
latestWinBoard = -1
boardsList = []
newBoard = []
for i in range(len(data)):
    if (len(newBoard) < 5):
        newBoard.append(data[i])
    else:
        boardsList.append(newBoard)
        newBoard = []
        newBoard.append(data[i])

def checkForWin(latestBoard, latestRow, latestCol):
    
    # Check if that native row results in a win
    allWinningTiles = True
    for i in range(5):
        print(f"Row Check: {boardsList[latestBoard][latestRow][i]}")
        if boardsList[latestBoard][latestRow][i][0] != '#':
            allWinningTiles = False
            
    if allWinningTiles == True:
        printWinAndScore(latestBoard, latestRow, latestCol)
        return True

    # Check if that native column results in a win
    allWinningTiles = True
    for i in range(5):
        print(f"Col Check: {boardsList[latestBoard][i][latestCol]}")
        if boardsList[latestBoard][i][latestCol][0] != '#':
            allWinningTiles = False
            
    if allWinningTiles == True:
        printWinAndScore(latestBoard, latestRow, latestCol)
        return True
    
    return False

def printWinAndScore(board, winningRow, winningCol):
    sumScore = 0
    for i in range(5):
        for j in range(5):
            if boardsList[board][i][j][0] != '#':
                sumScore += int(boardsList[board][i][j])

    finalScore = sumScore * int(boardsList[board][winningRow][winningCol].replace('#',''))
    print(f"FOUND WIN with score: {finalScore}")
    print(f"Winning Board: {boardsList[board]}")

def playGame():
    # Play the Game until Win
    for i in range(len(firstLine)):
        print(f"Checking val {i}:{firstLine[i]}")
        
        for board in range(len(boardsList)):
            if not board in boardsAlreadyWon:
                for row in range(len(boardsList[board])):
                    for col in range(len(boardsList[board][row])):
                        if firstLine[i] == boardsList[board][row][col]:
                            print(f"Found match {firstLine[i]} == {boardsList[board][row][col]} in board {board} at row {row} col {col} on turn {i}")
                            boardsList[board][row][col] = f"#{boardsList[board][row][col]}"
                            if checkForWin(board,row,col):
                                boardsAlreadyWon.append(board)

playGame()