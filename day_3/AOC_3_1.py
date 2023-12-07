from pprint import pprint

def is_symbol(c):
    return not ( c == '.' or c.isdigit() )

# checks surrounding cells for validity and presence of symbols
def valid_digit(matrix, y, x):
    # top left
    if x-1 >= 0 and y-1 >= 0 and is_symbol(matrix[y-1][x-1]):
        return True
    # top
    if y-1 >= 0 and is_symbol(matrix[y-1][x]):
        return True
    # top right
    if x+1 < len(matrix[y]) and y-1 >= 0 and is_symbol(matrix[y-1][x+1]):
        return True
    # right
    if x+1 < len(matrix[y]) and is_symbol(matrix[y][x+1]):
        return True
    # bottom right
    if x+1 < len(matrix[y]) and y+1 < len(matrix) and is_symbol(matrix[y+1][x+1]):
        return True
    # bottom
    if y+1 < len(matrix) and is_symbol(matrix[y+1][x]):
        return True
    # bottom left
    if x-1 >= 0 and y+1 < len(matrix) and is_symbol(matrix[y+1][x-1]):
        return True 
    # left
    if x-1 >= 0 and is_symbol(matrix[y][x-1]):
        return True
    return False

filename = "AOC_3.txt"
#filename = "AOC_3_test.txt"

matrix = []

with open(filename) as f:
    total = 0
    lines = f.readlines() 
    for line in lines:
        matrix.append([*line.strip()])

pprint(matrix)

# creates number as we go
number_tracker = 0
# tracks whether number is valid by checking if surrounding cells contain symbols
valid_flag = False

total = 0

# only have to go through the matrix once + up to 8 extra reads per digit in the matrix (should be much less than that)
for y, row in enumerate(matrix):
    print(f"row: {y+1}")
    for x, c in enumerate(row):
        if c.isdigit():
            number_tracker = number_tracker*10 + int(c)
            if not valid_flag:
                valid_flag = valid_digit(matrix, y, x)
        else:
            if valid_flag:
                print(f"\t{number_tracker} valid")
                total += number_tracker
                valid_flag = False
            number_tracker = 0
    if valid_flag:
        print(f"\t{number_tracker} valid")
        total += number_tracker
        valid_flag = False
    number_tracker = 0

print(total)
























