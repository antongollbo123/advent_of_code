
def part_1(text_content:str ) -> int:
    nums = text_content.split("\n")
    number_lists = []
    for i in nums:
        int_num_list = [int(ele) for ele in i.split()]
        number_lists.append(int_num_list)
    tot_sum = 0
    for number_list in number_lists:
        difference = [-1]
        while any (diff!= 0 for diff in difference):
            tot_sum += number_list[-1]
            difference = [number_list[i+1] - number_list[i] for i in range(len(number_list)-1)]
            number_list = difference
    return tot_sum

def part_2(text_content:str) -> int:
    nums = text_content.split("\n")
    number_lists = []
    for i in nums:
        int_num_list = [int(ele) for ele in i.split()]
        number_lists.append(int_num_list)
    tot_sum = 0
    return tot_sum

if __name__ == "__main__":
    filename = "sample_input.txt"
    with open(filename, "r") as file:
        content = file.read()
        output = part_1(text_content = content)
        print(output)
        output = part_2(text_content=content)
        print(output)

