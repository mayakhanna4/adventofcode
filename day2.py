
def main():
    num_valid = 0;
    input_file  = open("day2.txt")
    for line in input_file.readlines():
        first = int(line.split("-")[0])
        second = int(line.split("-")[1].split(" ")[0])
        char = line.split(":")[0][-1]
        word = line.split(":")[1]
        print(char)
        print(word[first])
        print(word[second])
        print(word[first] == char or word[second] == char)
        print(not(not(word[first] != char) and not(word[second] != char)))
        print("\n")
        if((word[first] == char or word[second] == char) and not(not(word[first] != char) and not(word[second] != char))):
            num_valid = num_valid + 1;

    print(num_valid)



if __name__ == "__main__":
    main()
