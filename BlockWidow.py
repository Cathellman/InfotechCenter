import glob
from time import sleep

defaultMap = [
        ['-','-','-','-','-'],
        ['-','-','-','-','-'],
        ['-','-','-','-','-'],
        ['-','-','-','-','-'],
        ['-','-','-','-','-'],
    ]

currentMap = [
        ['-','-','-','-','-'],
        ['-','-','-','-','-'],
        ['-','-','-','-','-'],
        ['-','-','-','-','-'],
        ['-','-','-','-','-'],
    ]

oldPos = [2,2]
currentPos = [2,2]

mapPos = [3,3]
mapTile = [0,0]

gasStationLocatons = [
        [-12, 78], 
        [45, -65], 
        [-34, 22], 
        [9, -87], 
        [-56, 33],
        [14, -99], 
        [72, 41], 
        [-88, -11],
        [66, -23], 
        [-91, 17], 
        [38, -45], 
        [25, 89], 
        [-73, -42], 
        [11, -63],
        [49, -54], 
        [-28, 76],
        [7, -39], 
        [-64, 21], 
        [85, -67], 
        [32, -88],
        [-19, 57], 
        [27, -82], 
        [-36, 45], 
        [10, -78],
        [91, 33], 
        [-22, 74], 
        [59, -61], 
        [-43, 29], 
        [18, -99], 
        [-75, 56]
    ]

locationsonScreenList = [
        [0, 0], [0, 0], [0, 0], [0, 0], 
        [0, 0], [0, 0], [0, 0], [0, 0],
        [0, 0], [0, 0], [0, 0], [0, 0], 
        [0, 0], [0, 0], [0, 0], [0, 0],
        [0, 0], [0, 0], [0, 0], [0, 0], 
        [0, 0], [0, 0], [0, 0], [0, 0],
        [0, 0]
    ]

def locationsOnScreen():
    startingNumber = []




def printMap():
    print('\n')
    print(mapPos)
    print(mapTile)
    for row in currentMap:
        for element in row:
            print(element, end=" ")
        print()
    sleep(0.5)
    
def reset():
   oldPos[0] = currentPos[0]
   oldPos[1] = currentPos[1]
   for i in range(len(defaultMap)):
    for j in range(len(defaultMap[0])):
        currentMap[i][j] = defaultMap[i][j]


def setPlayer():
    if currentPos[0] == 5:
        currentPos[0] = 0
        mapTile[1] -= 1
        
    if currentPos[1] == 5:
        currentPos[1] = 0
        mapTile[0] += 1
        

    if currentPos[0] == -1:
        currentPos[0] = 4
        mapTile[1] += 1
        

    if currentPos[1] == -1:
        currentPos[1] = 4
        mapTile[0] -= 1

    
    
    currentMap[currentPos[0]][currentPos[1]] = 'O'
    


def move():
    
    move = input('\n -> ')
    for i in move:
        if i == 'd':
            currentPos[1] += 1
            mapPos [0] += 1

        elif i == 'a':
            currentPos[1] -= 1
            mapPos [0] -= 1

        elif i == 's':
            currentPos[0] += 1
            mapPos [1] -= 1

        elif i == 'w':
            currentPos[0] -= 1
            mapPos [1] += 1


        setPlayer()
        printMap()
        reset()

setPlayer()
printMap()
reset()

while True:
    move()












