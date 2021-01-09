
def main():
    input_file  = open("day12.txt")
    list = []
    for line in input_file:
        list.append(line)
    dirs = {'E' : [1,0],'W':[-1,0],'N':[0,1],'S':[0,-1]}
    list_dirs=['E','N','W', 'S']
    way_cur_dir = 'E'
    cur_x = 0
    cur_y = 0
    way_x = 10
    way_y = 1
    for i in list:
        print(i)
        move_val = int(i[1:])
        if(i[0] == 'L'):
            # cur_dir = list_dirs[int((list_dirs.index(cur_dir) + move_val/90) % 4)]
            # print("NEW DIRECTIOn LEFT")
            # print(cur_dir)
            amount = move_val
            if(amount == 90):
                temp = way_x
                way_x = - way_y
                way_y =  temp
            elif(amount == 180):
                way_x = -way_x
                way_y = -way_y
            elif(amount == 270):
                temp = way_x
                way_x = way_y
                way_y = - temp
        elif(i[0] == 'R'):
            #cur_dir = list_dirs[int((list_dirs.index(cur_dir) - move_val/90) % 4)]
            # print("NEW DIRECTIOn RIGHT")
            # print(cur_dir)
            amount = 360 - move_val
            if(amount == 90):
                temp = way_x
                way_x = - way_y
                way_y = temp
            elif(amount == 180):
                way_x = -way_x
                way_y = -way_y
            elif(amount == 270):
                temp = way_x
                way_x = way_y
                way_y = - temp
        else:
            if(i[0] == 'F'):
                cur_x += move_val * (way_x)
                cur_y += move_val * (way_y)
            else:
                move_dir = dirs[i[0]]
                way_x += move_dir[0]*move_val
                way_y += move_dir[1]*move_val
        print("CUR")
        print(cur_x)
        print(cur_y)
        print("WAY")
        print(way_x)
        print(way_y)


if __name__ == "__main__":
    main()
