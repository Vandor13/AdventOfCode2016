from string import ascii_lowercase as alphabet


def shift(message, offset):
    trans = str.maketrans(alphabet, alphabet[offset:] + alphabet[:offset])
    return message.lower().translate(trans)


def get_most_common_letters(name):
    name = name.replace("-", "")
    letter_amount = dict()
    for char in name:
        if char in letter_amount.keys():
            letter_amount[char] = letter_amount[char] + 1
        else:
            letter_amount[char] = 1
    letters = sorted(letter_amount.keys())
    letter_ranking = sorted(letters, key=lambda character: letter_amount[character], reverse=True)
    # print(letter_ranking)
    return letter_ranking[:5]


def check_room(room: str):
    room = room.strip("\n")
    name = room[:-11]
    number, checksum = room.strip("]")[-9:].split("[")
    # print(f"Room {name} Number {number} Checksum {checksum}")
    real_checksum = "".join(get_most_common_letters(name))
    if real_checksum == checksum:
        return name, int(number)
    else:
        return None, None


class CheckSum:
    def __init__(self, filename):
        self.rooms = list()
        self.readfile(filename)
        self.real_rooms = []

    def readfile(self, filename):
        with open(filename, "r") as file:
            self.rooms = file.readlines()

    def sum_valid_rooms(self):
        sum_of_ids = 0
        for room in self.rooms:
            name, room_id = check_room(room)
            if room_id:
                sum_of_ids += room_id
                self.real_rooms.append((name, room_id))
        print("Sum of all valid room ids:", sum_of_ids)

    def decrypt_rooms(self):
        npo = None
        for room_name, room_id in self.real_rooms:
            decoded_name = shift(room_name, room_id % 26)
            print(decoded_name, room_id)
            if str(decoded_name).startswith("north"):
                npo = (decoded_name, room_id)
        print()
        print(npo)


check_sum = CheckSum("InputData/d4.txt")
check_sum.sum_valid_rooms()
check_sum.decrypt_rooms()
# print(shift("qzmt-zixmtkozy-ivhz", 343 % 26))
