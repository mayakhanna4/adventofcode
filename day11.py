def check_adj(x,y,list):
    fin = 0
    start_x = x
    start_y = y

    while(x-1 > -1):
        if(list[x - 1][y] == '#'):
            fin +=1
            break;
        if(list[x - 1][y] == 'L'):
            break;
        x = x - 1
    x = start_x
    while(y-1 > -1):
        if(list[x][y - 1] == '#'):
            fin +=1
            break;
        if(list[x][y - 1] == 'L'):
            break;
        y = y - 1
    y = start_y
    while(x-1 > -1 and y-1 > -1):
        if(list[x - 1][y - 1] == '#'):
            fin +=1
            break;
        if(list[x - 1][y - 1] == 'L'):
            break;
        x = x - 1
        y = y - 1
    x = start_x
    y = start_y
    while(x+1 < len(list) ):
        if(list[x + 1][y] == '#'):
            fin +=1
            break;
        if(list[x + 1][y] == 'L'):
            break;
        x = x + 1
    x = start_x
    while(y+1 < len(list[0])):
        if(list[x][y + 1] == '#'):
            fin +=1
            break;
        if(list[x][y + 1] == 'L'):
            break;
        y = y + 1
    y = start_y
    while(y+1 < len(list[0]) and x+1 < len(list) ):
        if(list[x + 1][y + 1 ] == '#'):
            fin +=1
            break;
        if(list[x + 1][y + 1] == 'L'):
            break;
        x = x + 1
        y = y + 1
    x = start_x
    y = start_y
    while(x-1 > -1 and y+1 < len(list[0])):
        if(list[x - 1][y + 1] == '#'):
            fin +=1
            break;
        if(list[x - 1][y + 1] == 'L'):
            break;
        x = x - 1
        y = y + 1
    x = start_x
    y = start_y
    while(x+1 < len(list) and y-1 > -1):
        if(list[x + 1][y -1] == '#'):
            fin +=1
            break;
        if(list[x + 1][y - 1] == 'L'):
            break;
        x = x + 1
        y = y -1
    x = start_x
    y = start_y
    print("X:" + str(start_x))
    print("Y:" + str(start_y))
    print("VAL" + str(fin))
    return fin


def main():
    input_file  = open("day11.txt")
    list = []
    for line in input_file:
        list.append(line)
    keep_going = True
    while keep_going:
        oldlist = list[:]
        for x in range(0,len(list)):
            print(list[x])
            for y in range(0,len(list[x])):
                if(list[x][y] == 'L'):
                    if(check_adj(x,y,oldlist) == 0):
                        list[x] = list[x][0:y] + "#" + list[x][y+1:]
                elif(list[x][y] == '#'):
                    if(check_adj(x,y,oldlist) >= 5):
                        list[x] = list[x][0:y] + "L" + list[x][y+1:]
        print(list)
        print(oldlist)
        if(oldlist == list):
            keep_going = False
    fin_occ = 0
    for x in range(0,len(list)):
        for y in range(0,len(list[x])):
            if(list[x][y] == '#'):
                fin_occ += 1
    print(fin_occ)






if __name__ == "__main__":
    main()
