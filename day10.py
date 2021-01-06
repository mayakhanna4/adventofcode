
branch_list = []
def determineWays(list):
    print(list)
    # global branch;
    # print("LIST")
    # print(list)
    # if(len(list) == 1):
    #     return;
    # cur_val = list[0]
    # i = 1;
    # while(i < len(list) and list[i] - cur_val <= 3):
    #     print("WE ARE BRANCHING TO:")
    #     print(list[i:])
    #     determineWays(list[i:])
    #     i = i + 1
    #     branch = branch + 1
    # print("BRANCH AFTER " +str(len(list)) )
    # print(branch)
    branch_list = [None] * len(list)
    branch_list[len(list)-1] = 1
    for i in range(len(list)-2, -1, -1):
        val = 0
        if(i+1 < len(list) and list[i+1] -list[i] <= 3):
            val = val + branch_list[i+1]
        if(i+2 < len(list) and list[i+2] -list[i] <= 3):
            val = val + branch_list[i+2]
        if(i+3 < len(list) and list[i+3] -list[i] <= 3):
            val = val + branch_list[i+3]
        branch_list[i] = val
    print(branch_list)
    print(branch_list[0])


def main():
    input_file  = open("day10.txt")
    list = []
    one_diff = 0
    three_diff = 0
    for line in input_file:
        list.append(int(line))
    list.append(0)
    list.sort()
    # current_val = 0
    # for i in range(0,len(list)):
    #     if(list[i] - current_val == 1):
    #         one_diff += 1
    #     elif(list[i] - current_val == 3):
    #         three_diff += 1
    #     current_val = list[i]
    #     print(current_val)
    # three_diff += 1
    # print(one_diff)
    # print(three_diff)
    determineWays(list)






if __name__ == "__main__":
    main()
