def calc_place(place, list):
    print("PLACE HERE")
    print(place)
    if(list[place].split(' ')[1][0] == '-'):
        place = place - int(list[place].split(' ')[1][1:]) % len(list)
        if(place < 0):
            place = len(list) + place
        # print("ENDING PLACE " + str(place))
    elif(list[place].split(' ')[1][0] == '+'):
        place = place + int(list[place].split(' ')[1][1:]) % len(list)
        if(place > len(list)):
            place =  place - len(list)
    return place;

def main():
    input_file  = open("day8.txt")
    list = []
    line_set = set()
    move_stack = []
    for line in input_file:
        list.append(line.strip())
        line_set.add(len(line_set))
    print("LIST SIZE " + str(len(list)))
    acc = 0
    place = 0
    while place < len(list):
        print(place)
        line_set.remove(place)
        if(list[place].split(' ')[0] == "acc"):
            if(list[place].split(' ')[1][0] == '+'):
                acc = acc + int(list[place].split(' ')[1][1:])
            else:
                acc = acc - int(list[place].split(' ')[1][1:])
            place = place + 1
        elif(list[place].split(' ')[0] == "jmp"):
            # print("STARTING PLACE " + str(place))
            move_stack.append(place)
            place = calc_place(place,list)
            # if(list[place].split(' ')[1][0] == '-'):
            #     place = place - int(list[place].split(' ')[1][1:]) % len(list)
            #     if(place < 0):
            #         place = len(list) + place
            #     # print("ENDING PLACE " + str(place))
            # elif(list[place].split(' ')[1][0] == '+'):
            #     place = place + int(list[place].split(' ')[1][1:]) % len(list)
            #     if(place > len(list)):
            #         place =  place - len(list)
                # print("ENDING PLACE " + str(place))
        elif(list[place].split(' ')[0] == "nop"):
            move_stack.append(list[place])
            place = place + 1
        if(place not in line_set): # we already seen this line, so we shouldnt go here
            print("YIKES")
            #(acc)
            find_in = move_stack.pop()
            print(find_in)
            print(type(find_in))
            val = calc_place(int(find_in),list)
            print(val)
            while ((val not in line_set) and not move_stack) :
                find_in = move_stack.pop()
            print("RESULT:")
            print(find_in)
            place = find_in

            break;
        if(place >= len(list)): #DONE
            print("DONE")
            print(acc)
            break;


if __name__ == "__main__":
    main()
