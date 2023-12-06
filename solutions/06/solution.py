import math
def part_1(text_content:str ) -> int:
    time, distance = text_content.split("\n")
    time, time_values = time.split(":")
    distance, distance_values = distance.split(":")
    time_values, distance_values = [int(ele) for ele in time_values.split()], [int(ele) for ele in distance_values.split()]
    num_record_beaters = []
    for time, distance in zip(time_values, distance_values):
        record_beater = 0
        for i in range(time):
            button_hold = i
            travel_distance = button_hold * (time - i)
            if travel_distance > distance:
                record_beater+=1
        num_record_beaters.append(record_beater)
    return math.prod(num_record_beaters)

def part_2(text_content:str ) -> int:
    text_content = "".join(text_content.replace(" ", ""))
    count_num_record_beaters = part_1(text_content=text_content)
    return count_num_record_beaters
    
if __name__ == "__main__":
    filename = "sample_input.txt"
    with open(filename, "r") as file:
        content = file.read()
        output = part_1(text_content = content)
        print(output)
        output = part_2(text_content=content)
        print(output)
