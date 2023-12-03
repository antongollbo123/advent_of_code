
def part_1(text_content:str, 
                   constraint: dict):
    
    line_content = text_content.split("\n")
    total_games_sum = 0
    for line in line_content:
        games_sum = 0
        info, sets = line.split(": ")
        possible_list = []
        for subset in sets.split(";"): 
            cube_count = subset.strip().split()

            strings_list = cube_count[1::2]  
            ints_list = [int(cube_count[i]) for i in range(0, len(cube_count), 2)] 

            for color, counter in zip(strings_list, ints_list):
                removed_commas = color.replace(",", "")
                if counter > constraint[removed_commas]:
                    possible_list.append(False)
                else:
                    possible_list.append(True)
        if False not in possible_list:
            total_games_sum += int(info.split(" ")[1])

        total_games_sum += games_sum

    return total_games_sum

def part_2(text_content:str, 
           constraint: dict):
    line_content = text_content.split("\n")
    total_sum = 0
    for line in line_content:
        games_sum = 0
        info, sets = line.split(": ")
        possible_list = []

        sets = sets.replace(";", "").replace(",", "")
        cube_count = sets.strip().split()

        strings_list = cube_count[1::2]  
        ints_list = [int(cube_count[i]) for i in range(0, len(cube_count), 2)] 

        color_max = {}

        for color, value in zip(strings_list, ints_list):
            # If the color is not in the dictionary or the value is greater than the current max, update the max
            if color not in color_max or value > color_max[color]:
                color_max[color] = value
        result = 1
        for value in color_max.values():
            result *= value
        total_sum += result
    return total_sum

if __name__ == "__main__":
    file_name = "real_input.txt"
    constraint = {'red': 12, 'green': 13, 'blue': 14}
    with open(file_name, 'r') as file:
        content = file.read()
        games_sum = part_1(text_content=content, constraint=constraint)
        print(f"The total games sum ::: {games_sum}")
        total_sum = part_2(text_content=content, constraint=constraint)
        print(f"The sum of the power of the sets ::: {total_sum}")

