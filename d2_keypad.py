KEYPAD = [
    ["0", "0", "1", "0", "0"],
    ["0", "2", "3", "4", "0"],
    ["5", "6", "7", "8", "9"],
    ["0", "A", "B", "C", "0"],
    ["0", "0", "D", "0", "0"]
]


class KeypadMoves:
    def __init__(self, filename="InputData/d2.txt"):
        self.instructions = []
        self.read_file(filename)
        self.code = ""
        self.previous_button = (2, 0)

    def find_code(self):
        for instruction in self.instructions:
            self.execute_instruction(instruction)
        print("Code is:", self.code)

    def execute_instruction(self, instruction: str):
        current_button = self.previous_button
        for char in instruction.strip("\n"):
            if char == "U":
                possible_button = (
                    max(current_button[0] - 1, 0),
                    current_button[1]
                )
            elif char == "L":
                possible_button = (
                    current_button[0],
                    max(current_button[1] - 1, 0)
                )
            elif char == "R":
                possible_button = (
                    current_button[0],
                    min(current_button[1] + 1, 4)
                )
            else:
                possible_button = (
                    min(current_button[0] + 1, 4),
                    current_button[1]
                )
            keypad_value = KEYPAD[possible_button[0]][possible_button[1]]
            if keypad_value != "0":
                current_button = possible_button
        self.previous_button = current_button
        self.code = self.code + KEYPAD[current_button[0]][current_button[1]]

    def read_file(self, filename):
        with open(filename, "r") as file:
            self.instructions = file.readlines()


code_finder = KeypadMoves("InputData/d2.txt")
code_finder.find_code()
