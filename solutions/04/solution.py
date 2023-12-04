from collections import defaultdict

def part_1(text_content:str ) -> int:
    separate_games = text_content.split("\n")
    tot_sum = 0
    for line in separate_games:
        game_no, game_content = line.split(":")
        winning_numbers, my_numbers = game_content.split("|")
        winning_numbers_list, my_numbers_list = [int(ele) for ele in winning_numbers.split()], [int(ele) for ele in my_numbers.split()]
        x, y = set(winning_numbers_list), set(my_numbers_list)
        z = x.intersection(y)
        exponent = len(z) - 1 
        if exponent == -1:
            tot_sum += 0
        else:
            tot_sum+= 2**exponent
    tot_sum = int(tot_sum)
    return tot_sum

def part_2(text_content:str) -> int:
    separate_games = text_content.split("\n")
    num_games = len(separate_games)
    card_count = [1] * num_games 

    for line_index, line in enumerate(separate_games):
        game_no, game_content = line.split(":")
        winning_numbers, my_numbers = game_content.split("|")
        winning_numbers_list, my_numbers_list = [int(ele) for ele in winning_numbers.split()], [int(ele) for ele in my_numbers.split()]
        x, y = set(winning_numbers_list), set(my_numbers_list)
        z = x.intersection(y)

        for match in range(len(z)):
            num_sc = card_count[line_index] # num scratchcards for this card, 
            match_length = line_index + match + 1 # How far we should check in the summing list
            card_count[match_length] += num_sc # how many scratchcards should we append of this card, to other cards that match?
    return sum(card_count)



if __name__ == "__main__":
    file_name = "sample_input.txt"
    with open(file_name, 'r') as file:
        content = file.read()
        games_sum = part_1(text_content=content)
        print(f"The total games sum ::: {games_sum}")
        scratchcard_sum = part_2(text_content=content)
        print(f"The scratchcard sum ::: {scratchcard_sum}")
        scratchcard_sum = part_2(text_content=content)
