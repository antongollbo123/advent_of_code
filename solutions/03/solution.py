import math as m, re

def part_1(text_content:str) -> int:
    
    grid = text_content.split("\n")
    grid_size = len(grid)
    non_numeric_indices = []

    for grid_row in range(grid_size):
          for grid_col in range(grid_size):
            if not re.match(r'[0123456789.]', grid[grid_row][grid_col]):
                    non_numeric_indices.append((grid_row,grid_col))
    tot_sum = 0
    for row_count, row in enumerate(grid):
        for numeric_value in re.finditer(r'\d+', row):
            numeric_value_edge_list = []

            for possible_row in (row_count-1, row_count, row_count+1):
                for possible_column in range(numeric_value.start()-1, numeric_value.end()+1):
                    numeric_value_edges = (possible_row,possible_column)
                    numeric_value_edge_list.append(numeric_value_edges)


            for edge in numeric_value_edge_list:
                if edge in non_numeric_indices:
                    tot_sum += int(numeric_value[0])
    return tot_sum

def part_2(text_content:str) -> int:
    grid = text_content.split("\n")
    grid_size = len(grid)
    non_numeric_indices = []
    
    for grid_row in range(grid_size):
          for grid_col in range(grid_size):
            if re.match(r'[*]', grid[grid_row][grid_col]):
                    non_numeric_indices.append((grid_row,grid_col))
    gear_ratio_sum = 0                
    gear_match_dict = {}
    for row_count, row in enumerate(grid):
        for numeric_value in re.finditer(r'\d+', row):
            numeric_value_edge_list = []

            for possible_row in (row_count-1, row_count, row_count+1):
                for possible_column in range(numeric_value.start()-1, numeric_value.end()+1):
                    numeric_value_edges = (possible_row,possible_column)
                    numeric_value_edge_list.append(numeric_value_edges)

            for edge in numeric_value_edge_list:
                if edge in non_numeric_indices:
                    if edge in gear_match_dict.keys():
                        gear_match_dict[edge].append(int(numeric_value[0]))
                    else:
                        gear_match_dict[edge] = [int(numeric_value[0])]
                    
    for value in gear_match_dict.values():
        if len(value) == 2:
            gear_ratio_sum += m.prod(value)
    return gear_ratio_sum

if __name__ == "__main__":
    filename ="real_input.txt"
    with open(filename, "r") as file:
        content = file.read()
        games_sum = part_1(text_content=content)
        print(f"The sum of all part numbers ::: {games_sum}")
        total_sum = part_2(text_content=content,)
        print(f"The sum of the gear ratios ::: {total_sum}")
        sol2 = part_2(text_content=content)

    