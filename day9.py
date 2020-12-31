# def sums(list, num):
#     print(list)
#     print(num)
#     for i in range(0,len(list))
#
#             return True
#     return False

def main():
    input_file  = open("day9.txt")
    list = []
    for line in input_file:
        list.append(int(line))
    # for i in range(25,len(list)):
    #     if(sums(list[i-25:i],list[i]) == False):
    #         print(list[i])
    #         print("DONE")
    #         break;
    #     break;
    for i in range(0,len(list)):
        cur_sum = list[i]
        place = i + 1
        while(cur_sum < 27911108 and place < len(list)):
            cur_sum = cur_sum + list[place]
            place = place + 1
        if(cur_sum == 27911108):
            print("DONE")
            print(i)
            print(place - 1)
            print(list[i])
            print(list[place-1])
            print(list[i:place])
            max= 0
            min = 10000000000000
            total_sum = 0
            for i in list[i:place]:
                total_sum = total_sum + i
                if(i > max):
                    max = i
                if(i < min):
                    min = i

            print(max+min)
            print(total_sum)







if __name__ == "__main__":
    main()
