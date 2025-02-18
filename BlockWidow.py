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

global gx
global gy
gx = 0
gy = 0


def printMap():
    print('\n', currentPos)
    print('\n')
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
        #gx += 1

    if currentPos[1] == 5:
        currentPos[1] = 0
        #gy += 1

    if currentPos[0] == -1:
        currentPos[0] = 4
        #gx -= 1

    if currentPos[1] == -1:
        currentPos[1] = 4
       # gy -= 1
    
    print(currentPos)
    currentMap[currentPos[0]][currentPos[1]] = 'O'
    


def move():
    
    move = input('\n -> ')
    for i in move:
        if i == 'd':
            currentPos[1] += 1

        elif i == 'a':
            currentPos[1] -= 1

        elif i == 's':
            currentPos[0] += 1

        elif i == 'w':
            currentPos[0] -= 1
        setPlayer()
        printMap()
        reset()

setPlayer()
printMap()
reset()

while True:
    move()












