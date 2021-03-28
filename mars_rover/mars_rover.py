from typing import List, Tuple


class Rover:
    def __init__(
        self,
        start_position: Tuple[float, float, str],
        grid_dimensions: Tuple[float, float],
    ) -> None:

        self.x = start_position[0]
        self.y = start_position[1]
        self.compass_to_angle = {"N": 90, "E": 0, "S": 270, "W": 180}
        self.angle = self.compass_to_angle[start_position[2]]
        self.angle_to_compass = {v: k for k, v in self.compass_to_angle.items()}
        self.max_x, self.max_y = grid_dimensions

    @property
    def position(self) -> Tuple[float, float, str]:
        return (self.x, self.y, self.angle_to_compass[self.angle])

    def instruct(self, instructions: List[str]) -> None:
        for instruction in instructions:
            if instruction in ["F", "B"]:
                self.move(direction=instruction)
            else:
                self.rotate(direction=instruction)

    def move(self, direction: str) -> None:
        distance = 1 if direction == "F" else -1

        if self.angle in (0, 180):
            self.move_along_x(distance)
        else:
            self.move_along_y(distance)

    def rotate(self, direction: str) -> None:
        turn = 90 if direction == "L" else -90
        self.angle = (self.angle + turn) % 360

    def move_along_x(self, distance: int) -> None:
        x_distance = self.rover_distance_to_x_distance(distance)
        if self.x == self.max_x and x_distance == 1:
            self.x = 1
        elif self.x == 0 and x_distance == -1:
            self.x = self.max_x - 1
        else:
            self.x += x_distance

    def move_along_y(self, distance: int) -> None:
        y_distance = self.rover_distance_to_y_distance(distance)
        if self.y == self.max_y and y_distance == 1:
            self.y = 1
        elif self.y == 0 and y_distance == -1:
            self.y = self.max_y - 1
        else:
            self.y += y_distance

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
