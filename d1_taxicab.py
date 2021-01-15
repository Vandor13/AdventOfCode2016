DEBUG = True
PART2 = True

NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class TaxiCab:

    def __init__(self, filename="InputData/d1.txt"):
        self.instructions = []
        self.read_file(filename)
        self.position = (0, 0)
        self.all_positions = set(self.position)
        self.direction = 0  # North
        self.follow_instructions()

    def read_file(self, filename):
        with open(filename, "r") as file:
            self.instructions = file.readline().replace(",", "").split()

    def follow_instructions(self):
        for instruction in self.instructions:
            self.execute_instruction(instruction)
        print("Last position:", self.position)
        print("Distance from start:", abs(self.position[0]) + abs(self.position[1]))

    def execute_instruction(self, instruction: str):
        if instruction[0] == "R":
            self.direction = (self.direction + 1) % 4
        else:
            self.direction = (self.direction - 1) % 4
        no_blocks = int(instruction.lstrip("RL"))
        for i in range(no_blocks):
            self.position = (
                    self.position[0] + DIRECTIONS[self.direction][0],
                    self.position[1] + DIRECTIONS[self.direction][1]
            )
            if self.position in self.all_positions and PART2:
                print("Crossed paths at:", self.position)
                print("Distance to start:", abs(self.position[0]) + abs(self.position[1]))
                exit()
            else:
                self.all_positions.add(self.position)
        if DEBUG:
            print("Now at:", self.position)


taxi_cab = TaxiCab("InputData/d1.txt")