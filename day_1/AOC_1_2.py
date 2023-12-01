filename = "AOC_1.txt"
#filename = "AOC_1_test.txt"
with open(filename) as f:
    total = 0
    lines = f.readlines() 
    for line in lines:
        # since I already have a working, tested script that finds digits, I decided to just build off of that
        # the input file is only 1000 lines long so I chose speed of development over maximum efficiency. 
        # replace function built in to python works well and is wasy to use.
        # the one issue I ran into was situations like "eighthree" where we needed to see eight before three. 
        # I considered changing course and scanning from left to right and then right to left checking for spelled out digits.
        # instead I just decided to replace "three" with "three3three"
        # this both adds the nuumber for my original script to identify, and preserves the inital 't' so that when we get to eight it still recognizes it. 
        # definintely not the most efficient, but easy to code and for input sizes this small there is no need for anthing else. 

        #track original line for sanity check later
        old_line = line
        
        line = line.replace("one", "one1one")
        line = line.replace("two", "two2two")
        line = line.replace("three", "three3three")
        line = line.replace("four", "four4four")
        line = line.replace("five", "five5five")
        line = line.replace("six", "six6six")
        line = line.replace("seven", "seven7seven")
        line = line.replace("eight", "eight8eight")
        line = line.replace("nine", "nine9nine")
        
        index = 0
        tens = None
        ones = None

        # from left to right search char by char until a digit is found
        while tens == None and index < len(line):
            if line[index].isdigit():
                tens = int(line[index])
            else:
                index += 1
        
        # from right to left search char by char until a digit is found
        index = len(line) - 1
        while ones == None and index >= 0:
            if line[index].isdigit():
                ones = int(line[index])
            else:
                index -= 1

        # sanity check 
        print(f"{tens}{ones}: {line} {old_line}")

        # digit found check
        if tens != None and ones != None:
            total += tens*10 + ones
    print(f"total: {total}")

