import glob
import random
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

mapTileCount = [0,0]
mapPos = [3,3]
mapTile = [0,0]

global onPlace
onPlace = False

gasStationLocatons = [
        [-12, 78], 
        [45, -65], 
        [-34, 22], 
        [9, 9], 
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
        [1, 5], 
        [1, 4], 
        [1, 3], 
        [1, 2], 
        [1, 1],
        [2, 5], 
        [2, 4], 
        [2, 3], 
        [2, 2], 
        [2, 1],
        [3, 5], 
        [3, 4], 
        [3, 3], 
        [3, 2], 
        [3, 1],
        [4, 5], 
        [4, 4], 
        [4, 3], 
        [4, 2], 
        [4, 1],
        [5, 5], 
        [5, 4], 
        [5, 3], 
        [5, 2], 
        [5, 1]
    ]

currentGasStationslist = [
        [9,9,'Shell']
    ]

def locationsOnScreen():
    k = 0
    while k < mapTile[0] and mapTile[0] > 0:
       k += 1
       
       for value in locationsonScreenList:
            value[0] = value[0] + 5
    
    k = 0
    while k > mapTile[0] and mapTile[0] < 0:
       k -= 1
       for value in locationsonScreenList:
            value[0] = value[0] - 5

    k = 0
    while k < mapTile[1] and mapTile[1] > 0:
        k += 1
        
        for value in locationsonScreenList:
            value[1] = value[1] + 5

    k = 0
    while k > mapTile[1] and mapTile[1] < 0:
        k -= 1
        
        for value in locationsonScreenList:
            value[1] = value[1] - 5


    mapTileCount[0] += mapTile[0]
    mapTileCount[1] += mapTile[1]
    
    mapTile[0] = 0
    mapTile[1] = 0

    """
    print the location on screen list 

    for i in range(5):
        for j in range(5):
            print(locationsonScreenList[i * 5 + j], end=' ')
        print()
    """

    for value in locationsonScreenList:
        x = value[0]
        y = value[1]
        
        for place in gasStationLocatons:
            xP = place[0]
            yP = place[1]
            
            if x == xP and y == yP:
                xP = (xP -(mapTileCount[0]*5)) -1
                yP = (yP -(mapTileCount[0]*5)) -1
               
                

                currentMap[xP][yP] = '=' 


def printMap():
    print('\n')
    print(mapPos)
    
    for row in currentMap:
        for element in row:
            print(element, end=" ")
        print()
    sleep(0.3)
    
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

    
    if currentMap[currentPos[0]][currentPos[1]] == '=':
        global onPlace
        onPlace = True
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
        
        locationsOnScreen()
        setPlayer()
        printMap()
        reset()
        
def place():
    if onPlace:
        print('You have landed on a gas station')
        for gasStatin in currentGasStationslist:
            print(gasStatin[0],gasStatin[1],gasStatin[2])
            if gasStatin[0] == mapPos[0] and gasStatin[1] == mapPos[1]:
                print('\n'+gasStatin[3])
                print('Working')
                sleep(4)
            else:
                newRow = [currentPos[0],currentPos[1],random.choice(['Shell', 'Chevron', 'Exxon', 'BP', 'Sunoco', 'Mobil', 'Valero'])]
                currentGasStationslist.append(newRow)
                for gasStatin in currentGasStationslist:
                    if gasStatin[0] == mapPos[0] and gasStatin[1] == mapPos[1]:
                        print(currentGasStationslist)
                        sleep(5)
                        print('\n'+gasStatin[2])
                        print('Working2')
                        sleep(4)



setPlayer()
printMap()
reset()

while True:
    place()
    move()












