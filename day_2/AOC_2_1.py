filename = "AOC_2.txt"
#filename = "AOC_2_test.txt"
with open(filename) as f:
    sum_of_games = 0
    games = f.readlines()
    for game in games:
        game_name = game.split(':')[0]
        game_data = game.split(':')[1]
        game_id = int(game_name.split()[1].strip())
        rounds = game_data.split(';')

        # track min number of cubes possible in bag with given knowledge
        min_colors = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        # go through each round and update min values
        for round in rounds:
            colors = round.split(',')
            for color in colors:
                color_name = color.split()[1]
                cube_count = int(color.split()[0].strip())
                if min_colors[color_name] < cube_count:
                    min_colors[color_name] = cube_count

        # check that values are within scenario constraints
        red_check = min_colors['red'] <= 12
        green_check = min_colors['green'] <= 13
        blue_check = min_colors['blue'] <= 14

        # sanity check 
        print(f"{game_name}: {red_check and green_check and blue_check}\n\t{min_colors}")

        # add game id to sum if valid
        if red_check and green_check and blue_check:
            sum_of_games += game_id

    # result output
    print(f"sum of the IDs: {sum_of_games}")