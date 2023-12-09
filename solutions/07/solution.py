from collections import Counter


def part_1(text_content: str, mode:int=1) -> int:
    letter_strength_map = {
        "A": "A",
        "K": "B",
        "Q": "C",
        "J": "D",
        "T": "E",
        "9": "F",
        "8": "G",
        "7": "H",
        "6": "I",
        "5": "J",
        "4": "K",
        "3": "L",
        "2": "M",
    }
    text_content = text_content.split("\n")
    value_map_dict = {
        "[5]": 6,
        "[4, 1]": 5,
        "[3, 2]": 4,
        "[3, 1, 1]": 3,
        "[2, 2, 1]": 2,
        "[2, 1, 1, 1]": 1,
        "[1, 1, 1, 1, 1]": 0,
    }
    hand_value_dict = {}
    hand_bid_map = {}
    for line in text_content:
        hand, bid = line.split()
        hand = "".join(
            idx if idx not in letter_strength_map else letter_strength_map[idx]
            for idx in hand
        )
        #if mode == 2:


        hand_bid_map[hand] = bid
        counter = Counter(hand)
        count = [i for i in counter.values()]
        #breakpoint()
        count.sort(reverse=True)
        hand_value_dict[hand] = value_map_dict[repr(count)]
    order_list = []
    for value in list(value_map_dict.values()):
        value_match = list(
            filter(lambda k: float(hand_value_dict[k]) == value, hand_value_dict)
        )
        if value_match:
            value_match.sort()
            order_list.extend(value_match)
    tot_sum = 0
    for i, k in enumerate(order_list):
        tot_sum += int(hand_bid_map[k]) * (len(text_content) - i)
    return tot_sum

def part_2(text_content:str) -> int:
    letter_strength_map = {
        "A": "A",
        "K": "B",
        "Q": "C",
        "J": "Z",
        "T": "E",
        "9": "F",
        "8": "G",
        "7": "H",
        "6": "I",
        "5": "K",
        "4": "L",
        "3": "M",
        "2": "N" 
    }
    text_content = text_content.split("\n")
    value_map_dict = {
        "[5]": 6,
        "[4, 1]": 5,
        "[3, 2]": 4,
        "[3, 1, 1]": 3,
        "[2, 2, 1]": 2,
        "[2, 1, 1, 1]": 1,
        "[1, 1, 1, 1, 1]": 0,
    }
    hand_value_dict = {}
    hand_bid_map = {}
    for line in text_content:
        hand, bid = line.split()
        hand = "".join(
            idx if idx not in letter_strength_map else letter_strength_map[idx]
            for idx in hand
        )
        counter = Counter(hand)
        if "Z" in hand:
            if counter[max(counter, key=counter.get)] > 1:
                
                hand = hand.replace("Z","D")
                value_add = hand.count("D")
                hand = hand.replace("D", "")
                if(hand == "LDDCC"):
                    breakpoint()
                counter[max(counter, key=counter.get)] += hand.count("D")
                counter.pop("Z")
        hand_bid_map[hand] = bid
        count = list(counter.values())
        count.sort(reverse=True)
        try:    
            hand_value_dict[hand] = value_map_dict[repr(count)]
        except:
            breakpoint()
        if(hand=="FDFFF"):
            breakpoint()
    order_list = []
    for value in list(value_map_dict.values()):
        value_match = list(
            filter(lambda k: float(hand_value_dict[k]) == value, hand_value_dict)
        )
        if value_match:
            value_match.sort()
            order_list.extend(value_match)
    tot_sum = 0
    for i, k in enumerate(order_list):
        tot_sum += int(hand_bid_map[k]) * (len(text_content) - i)
    return tot_sum


if __name__ == "__main__":
    file_name = "real_input.txt"
    with open(file_name, "r") as file:
        content = file.read()
        games_sum = part_1(text_content=content)
        print(f"TOTAL WINNINGS ::: {games_sum}")
        games_sum2 = part_2(text_content=content)
        print(f"TOTAL WINNINGS, PART 2 ::: {games_sum2 == 251515496}")
