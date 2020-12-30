inputList = []
with open("day3.txt","r") as f:
    for line in f:
        inputList.append(line)

xMax = int(len(inputList[0])-1)

def slope(xIncrement, yIncrement):
    posX = 0;
    posY = 0;
    trees = 0;

    while posY < len(inputList):
        if inputList[posY][posX] == "#":
            trees += 1
        posX += xIncrement
        posY += yIncrement
        if posX >= xMax:
            posX -= xMax

    return trees

print("Part 1: "+str(slope(3,1)))
print(slope(1,1))
print(slope(3,1))
print(slope(5,1))
print(slope(7,1))
print(slope(1,2))
print("Part 2: "+str(slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2)))
