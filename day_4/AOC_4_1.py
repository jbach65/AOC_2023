filename = "AOC_4.txt"
#filename = "AOC_4_test.txt"
with open(filename) as f:
    total = 0
    lines = f.readlines() 
    for line in lines:
        card_string = line.split(':')[0]
        card_num = int(card_string.split()[1])
        card_name = "Card " + str(card_num)
        data = line.split(':')[1]
        winning = data.split('|')[0].strip().split()
        mine = data.split('|')[1].strip().split()
        intersection_count = len(set(winning) & set(mine))
        points = 0
        if intersection_count > 0:
            points = pow(2,intersection_count-1)
        print(card_name, winning, mine, intersection_count)
        total+=points
    print(total)