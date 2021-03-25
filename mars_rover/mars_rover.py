from typing import List, Tuple


class Rover:
    def __init__(self, start_position: Tuple[float, float, str]) -> None:
        self.x = start_position[0]
        self.y = start_position[1]
        self.compass_to_angle = {"N": 90, "E": 0, "S": 270, "W": 180}
        self.angle_to_compass = {v: k for k, v in self.compass_to_angle.items()}
        self.angle = self.compass_to_angle[start_position[2]]

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
        if self.angle == 0:
            self.x += distance
        elif self.angle == 90:
            self.y += distance
        elif self.angle == 180:
            self.x -= distance
        else:
            self.y -= distance

    def rotate(self, direction: str) -> None:
        turn = 90 if direction == "L" else -90
        self.angle = (self.angle + turn) % 360
