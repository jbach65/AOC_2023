filename = "AOC_2.txt"
#filename = "AOC_2_test.txt"
with open(filename) as f:
    sum_of_power = 0
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

        # multiply min values together to get power
        power = min_colors['red'] * min_colors['green'] * min_colors['blue']

        # add power to sum
        sum_of_power += power

        # sanity check 
        print(f"{game_name}: {power}\n\t{min_colors}")

    # result output
    print(f"sum of the power: {sum_of_power}")