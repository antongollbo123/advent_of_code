def part_1(text_content:str) -> int:
    search_pattern, content = text_content.split("\n\n")
    individual_node = content.split("\n")
    node_dict = {}
    for item in individual_node:
        key,value = item.strip().split(" = ")
        value_tuple = tuple(element.strip() for element in value.strip('()').split(','))
        node_dict[key] = value_tuple
    num_steps = 0
    answer = "AAA"
    while answer != "ZZZ":
        pattern = search_pattern[num_steps % len(search_pattern)]
        if pattern == "L":
            answer = node_dict[answer][0]
        elif pattern == "R":
            answer = node_dict[answer][1]
        num_steps += 1
    return num_steps

if __name__ == "__main__":
    filename = "real_input.txt"
    with open(filename, "r") as file:
        content = file.read()
        output = part_1(text_content = content)
        print(output)
        #output = part_2(text_content=content)
       #print(output)