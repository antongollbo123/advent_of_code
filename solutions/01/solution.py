def part_1(text_content: str) -> int:
    tot_sum = 0
    for line in text_content.split("\n"):
        num_list = [int(char) for char in line if char.isdigit()]
        if len(num_list) > 0:
            tot_sum += int(str(num_list[0]) + str(num_list[-1]))
    return tot_sum


def part_2(text_content: str) -> str:
    mapper_dict = {
        "one": "o1e",
        "two": "t2o",
        "three": "th3ee",
        "four": "f4ur",
        "five": "f5ve",
        "six": "s6x",
        "seven": "se7en",
        "eight": "ei8ht",
        "nine": "n9ne",
    }
    for digit_word, new_digit_word in mapper_dict.items():
        text_content = text_content.replace(digit_word, new_digit_word) 
    tot_sum = part_1(text_content=text_content)
    return tot_sum


if __name__ == "__main__":
    file_name = "real_input.txt"
    with open(file_name, "r") as file:
        content = file.read()
        sum_of_two_digit_numbers = part_1(text_content=content)
        print(f"SUM OF TWO DIGIT NUMBERS ::: {sum_of_two_digit_numbers}")
        sum_of_two_digit_numbers2 = part_2(text_content=content)
        print(f"SUM OF TWO DIGIT NUMBERS, PART 2 ::: {sum_of_two_digit_numbers2}")
