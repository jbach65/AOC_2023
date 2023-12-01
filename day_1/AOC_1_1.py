filename = "AOC_1.txt"
#filename = "AOC_1_test.txt"
with open(filename) as f:
    total = 0
    lines = f.readlines() 
    for line in lines:
        index = 0
        tens = None
        ones = None
        
        # from left to right search char by char until a digit is found
        while tens == None and index < len(line):
            if line[index].isdigit():
                tens = int(line[index])
            index += 1
        

        # from right to left search char by char until a digit is found
        index = len(line) - 1
        while ones == None and index >= 0:
            if line[index].isdigit():
                ones = int(line[index])
            else:
                index -= 1
        
        #sanity check logging
        print(f"{tens}{ones}: {line}")

        # this just ensures that at least one number was found
        if tens != None and ones != None:
            total += tens*10 + ones
    print(f"total: {total}")
