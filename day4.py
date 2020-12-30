import re
def main():
    num_valid = 0;
    input_file  = open("day4.txt")
    valid_set = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    my_set = {}
    for line in input_file.readlines():
        if(line == "\n"):
            #check if valid
            if(len(valid_set) == 0):
                num_valid = num_valid + 1
            valid_set = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        else:
            result = re.split(':', line.replace(' ',':'))
            for i in range(0,len(result)):
                if(result[i] in valid_set):
                    if(result[i] == "byr" and int(result[i+1]) <=2002 and int(result[i+1]) >= 1920):
                        valid_set.remove(result[i])
                    if(result[i] == "iyr" and int(result[i+1]) <=2020 and int(result[i+1]) >= 2010):
                        valid_set.remove(result[i])
                    if(result[i] == "eyr" and int(result[i+1]) <=2030 and int(result[i+1]) >= 2020):
                        valid_set.remove(result[i])
                    if(result[i] == "hgt"):
                        type = result[i+1].strip()[-2:]
                        val = result[i+1].strip()[:-2]
                        # print("type " + type)
                        # print(" val " + val)
                        if(type == "cm" and int(val) <=193 and int(val) >= 150):
                            valid_set.remove(result[i])
                            print("HGT 1")
                        elif(type== "in" and int(val) <=76 and int(val) >= 59):
                            valid_set.remove(result[i])
                            print("HGT 2")
                    if(result[i] == "hcl"):
                        if(len(result[i+1].strip()) == 7 and result[i+1][0] =='#'):
                            all_cor = True
                            for el in result[i+1].strip():
                                if(not(el.isdigit() or el in ['a','b','c','d','e','f','#'])):
                                    print("Failed" + el)
                                    all_cor = False
                            if(all_cor):
                                valid_set.remove(result[i])
                    if(result[i] == "ecl"):
                        if(result[i+1].strip() in ["amb","blu", "brn", "gry", "grn", "hzl", "oth"]):
                            valid_set.remove(result[i])
                    if(result[i] == "pid" and len(result[i+1].strip()) == 9):
                        valid_set.remove(result[i])





    print(num_valid)



if __name__ == "__main__":
    main()
