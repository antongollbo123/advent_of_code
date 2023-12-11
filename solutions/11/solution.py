from itertools import combinations
from tqdm import tqdm
def part_1(text_content: str) -> int:
    lines = []
    for line in text_content.split("\n"):
        lines.append(line)
    empty_rows = []
    for y, row in enumerate(lines):
        if all(char == '.' for char in row):
            empty_rows.append(y)
    empty_cols = []
    for col_index in range(len(lines[0])):
        if all(row[col_index] == '.' for row in lines):
            empty_cols.append(col_index)
    expanded_coordinates_galaxy = []
    for y, row in enumerate(lines):
        for x, character in enumerate(row):
            if character == '#':
                empty_galaxy_cols = len([column for column in empty_cols if column < x])
                empty_galaxy_rows = len([row for row in empty_rows if row < y]) 
                new_x = x + ( empty_galaxy_cols * (1))
                new_y = y + (empty_galaxy_rows * (1))
                expanded_coordinates_galaxy.append((new_x, new_y))
    tot_sum = 0
    n = len(expanded_coordinates_galaxy)
    for i in range(n - 1):
        for j in range(i + 1, n):
            galaxy1, galaxy2 = expanded_coordinates_galaxy[i], expanded_coordinates_galaxy[j]
            tot_sum += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    return tot_sum

def part_2(text_content: str) -> int:
    lines = []
    for line in text_content.split("\n"):
        lines.append(line)
    empty_rows = []
    for y, row in enumerate(lines):
        if all(char == '.' for char in row):
            empty_rows.append(y)
    empty_cols = []
    for col_index in range(len(lines[0])):
        if all(row[col_index] == '.' for row in lines):
            empty_cols.append(col_index)
    expanded_coordinates_galaxy = []
    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            if char == '#':
                empty_galaxy_cols = len([column for column in empty_cols if column < x])
                empty_galaxy_rows = len([row for row in empty_rows if row < y]) 
                new_x = x + ( empty_galaxy_cols * (1_000_000 - 1))
                new_y = y + (empty_galaxy_rows * (1_000_000 - 1))
                expanded_coordinates_galaxy.append((new_x, new_y))
    tot_sum = 0
    n = len(expanded_coordinates_galaxy)
    for i in range(n - 1):
        for j in range(i + 1, n):
            galaxy1, galaxy2 = expanded_coordinates_galaxy[i], expanded_coordinates_galaxy[j]
            tot_sum += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    return tot_sum

if __name__ == "__main__":
    filename = "real_input.txt"
    with open(filename, "r") as file:
        content = file.read()
        output = part_1(text_content = content)
        print(output)
        output = part_2(text_content=content)
        print(output)

