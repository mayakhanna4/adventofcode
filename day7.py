total_count = set()
val_dict = {}

def find(line_list, to_look ):
    print('TO LOOK: ' + to_look)
    for i in line_list:
        print(i[1])
        if(i[1].find(to_look) != -1 ):
            print('in here')
            print(i[0].strip())
            if(i[1].strip() not in total_count):
                total_count.add(i[0].strip())
                find(line_list,i[0].strip())

def calc(val_list, to_look):
    track = 0;
    if(not val_list[to_look]):
        return 0;
    for key in val_list[to_look]:
            track = track  + int(key[0]) +  int(int(key[0]) * calc(val_list, key[1]))
    return track;



def main():
    input_file  = open("day7.txt")
    line_list = []
    val_list = {}
    for line in input_file.readlines():
        line_list.append(line.split('bags contain'))
        temp_dict = []
        for i in line.split('bags contain')[1].split(','):
            all_words = i.strip().split(' ')
            if(all_words[0] != "no"):
                temp_dict.append([all_words[0],all_words[1] + ' ' + all_words[2]])
        val_list[line.split('bags contain')[0].strip()] = temp_dict
    print(calc(val_list, 'shiny gold'))


if __name__ == "__main__":
    main()
