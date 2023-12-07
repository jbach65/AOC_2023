from pprint import pprint
filename = "AOC_4.txt"
#filename = "AOC_4_test.txt"
with open(filename) as f:
    lines = f.readlines() 
    card_dict= {}
    total_cards = 0
    for i, line in enumerate(lines):
        # split up data into manageable variables
        card_string = line.split(':')[0]
        card_num = int(card_string.split()[1])
        card_name = "Card " + str(card_num)
        data = line.split(':')[1]
        winning = data.split('|')[0].strip().split()
        mine = data.split('|')[1].strip().split()
        # find winning num count
        intersection_count = len(set(winning) & set(mine))
        # create dict entry if it does nat already exist
        if card_name not in card_dict:
            card_dict[card_name] = 0
        # account for original card
        card_dict[card_name] += 1

        print(card_name, card_dict[card_name], winning, mine, intersection_count)

        # add future cards
        for j in range(1, intersection_count+1):
            future_card_name = "Card " + str(i + 1 + j)
            if future_card_name not in card_dict:
                card_dict[future_card_name] = 0
            card_dict[future_card_name] += card_dict[card_name]
        # add total cards and copies to total
        total_cards += card_dict[card_name]

    print(total_cards)