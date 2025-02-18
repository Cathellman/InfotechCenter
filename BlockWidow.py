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



def printMap():
    print('\n')
    for row in currentMap:
        for element in row:
            print(element, end=" ")
        print()
    
def reset():
   oldPos[0] = currentPos[0]
   oldPos[1] = currentPos[1]
   for i in range(len(defaultMap)):
    for j in range(len(defaultMap[0])):
        currentMap[i][j] = defaultMap[i][j]


def setPlayer():
    currentMap[currentPos[0]][currentPos[1]] = 'O'
    print(oldPos)


def move():
    
    move = input('\n -> ')
    if move == 'd':
        currentPos[1] += 1

    elif move == 'a':
        currentPos[1] -= 1

    elif move == 's':
        currentPos[0] += 1

    elif move == 'w':
        currentPos[0] -= 1

while True:
    setPlayer()
    printMap()
    reset()
    move()












