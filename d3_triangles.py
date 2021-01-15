from itertools import combinations

PART2 = True

class Triangles:
    def __init__(self, filename):
        self.triangles = []
        if PART2:
            self.read_file_part_2(filename)
        else:
            self.read_file(filename)
        print("Number of all triangles:", len(self.triangles))
        self.remove_impossible_triangles()
        print("Number of correct triangles:", len(self.triangles))
        # for triangle in self.triangles:
        #     print(triangle)

    def read_file(self, filename):
        with open(filename, "r") as file:
            raw_triangles = file.readlines()
        for raw_triangle in raw_triangles:
            parts = raw_triangle.strip("\n").split()
            self.triangles.append([int(parts[0]), int(parts[1]), int(parts[2])])

    def read_file_part_2(self, filename):
        with open(filename, "r") as file:
            raw_triangles = file.readlines()
        for start_number in range(0, len(raw_triangles), 3):
            parts_1 = raw_triangles[start_number].strip("\n").split()
            parts_2 = raw_triangles[start_number + 1].strip("\n").split()
            parts_3 = raw_triangles[start_number + 2].strip("\n").split()
            self.triangles.append([int(parts_1[0]), int(parts_2[0]), int(parts_3[0])])
            self.triangles.append([int(parts_1[1]), int(parts_2[1]), int(parts_3[1])])
            self.triangles.append([int(parts_1[2]), int(parts_2[2]), int(parts_3[2])])

    def remove_impossible_triangles(self):
        for triangle in self.triangles.copy():
            for sides in combinations(range(3), 2):
                if triangle[sides[0]] + triangle[sides[1]] <= triangle[3 - sum(sides)]:
                    self.triangles.remove(triangle)
                    print("Impossible triangle:", triangle)
                    break


triangles = Triangles("InputData/d3.txt")
