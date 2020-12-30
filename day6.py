
def main():
    input_file  = open("day6.txt")
    our_set = set()
    total_sum = 0
    count = 0
    for line in input_file.readlines():
        if line.strip() == '':
            total_sum = total_sum + len(our_set)
            print(our_set)
            our_set = set()
            count = 0
        else:
            if(count == 0):
                for i in line.strip():
                    our_set.add(i)
                count = count + 1
            else:
                count = count + 1
                new_person_set = set()
                for i in line.strip():
                    new_person_set.add(i)
                our_set = our_set.intersection(new_person_set)



    print(total_sum + len(our_set) )


if __name__ == "__main__":
    main()
