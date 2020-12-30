
def main():
    input_file  = open("day5.txt")
    max_seat_id = 0
    list = []
    for line in input_file.readlines():
            new_line = line.strip()
            row_low = 0
            row_high = 127
            col_low = 0
            col_high = 7


            for i in range(7):
                mid = (int)(row_high + row_low)/ 2
                if(new_line[i] == 'F'):
                    row_high = mid
                elif(new_line[i] == 'B'):
                    row_low = mid + 1
            for i in range(7,10):
                mid = (int)(col_high + col_low)/ 2
                if(new_line[i] == 'L'):
                    col_high = mid
                elif(new_line[i] == 'R'):
                    col_low = mid +1
            cur_seat_id = row_high * 8 + col_high
            list.append(cur_seat_id )
            if(cur_seat_id > max_seat_id):
                max_seat_id = cur_seat_id
    list.sort()
    print(list)
    for i in range(46,915):
        if(i not in list):
            print(i)

if __name__ == "__main__":
    main()
