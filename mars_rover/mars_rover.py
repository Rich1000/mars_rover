from typing import List, Tuple


class Rover:
    def __init__(
        self,
        start_position: Tuple[int, int, str],
        grid_dimensions: Tuple[int, int],
        obstacles: List = [],
    ) -> None:

        self.x = start_position[0]
        self.y = start_position[1]
        self.compass_to_angle = {"N": 90, "E": 0, "S": 270, "W": 180}
        self.angle = self.compass_to_angle[start_position[2]]
        self.angle_to_compass = {v: k for k, v in self.compass_to_angle.items()}
        self.max_x, self.max_y = grid_dimensions
        self.obstacles = obstacles

    @property
    def position(self) -> Tuple[int, int, str]:
        return (self.x, self.y, self.angle_to_compass[self.angle])

    def instruct(self, instructions: List[str]) -> None:
        for instruction in instructions:
            if instruction in ["F", "B"]:
                new_coordinates = self.get_new_coordinates(direction=instruction)
                if new_coordinates in self.obstacles:
                    print(
                        f"Cannot proceed due to obstacle at position {new_coordinates}, "
                        f"stopped at position {self.position}"
                    )
                    break
                else:
                    self.x, self.y = new_coordinates
            else:
                self.rotate(direction=instruction)

    def get_new_coordinates(self, direction: str) -> Tuple[int, int]:
        distance = 1 if direction == "F" else -1

        if self.angle in (0, 180):
            new_x = self.new_x(distance)
            new_y = self.y
        else:
            new_x = self.x
            new_y = self.new_y(distance)

        return (new_x, new_y)

    def rotate(self, direction: str) -> None:
        turn = 90 if direction == "L" else -90
        self.angle = (self.angle + turn) % 360

    def new_x(self, distance: int) -> int:
        x_distance = self.rover_distance_to_x_distance(distance)
        if self.x == self.max_x and x_distance == 1:
            return 1
        elif self.x == 0 and x_distance == -1:
            return self.max_x - 1
        else:
            return self.x + x_distance

    def new_y(self, distance: int) -> int:
        y_distance = self.rover_distance_to_y_distance(distance)
        if self.y == self.max_y and y_distance == 1:
            return 1
        elif self.y == 0 and y_distance == -1:
            return self.max_y - 1
        else:
            return self.y + y_distance

    def rover_distance_to_x_distance(self, distance: int) -> int:
        if self.angle == 0:
            return distance
        else:
            return -distance

    def rover_distance_to_y_distance(self, distance: int) -> int:
        if self.angle == 90:
            return distance
        else:
            return -distance
