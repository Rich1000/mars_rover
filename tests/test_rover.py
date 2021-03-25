from mars_rover.mars_rover import Rover


def test_rover_reports_start_position():
    rover = Rover(start_position=(0, 0, "N"))
    assert rover.position == (0, 0, "N")


def test_rover_rotate():
    rover = Rover(start_position=(0, 0, "N"))

    rover.instruct(["L", "L"])
    assert rover.position == (0, 0, "S")

    rover.instruct(["R"])
    assert rover.position == (0, 0, "W")

    rover.instruct(["R", "R", "R", "R", "R"])
    assert rover.position == (0, 0, "N")


def test_rover_move_forward_and_back():
    rover = Rover(start_position=(0, 0, "N"))

    rover.instruct(["F"])
    assert rover.position == (0, 1, "N")

    rover.instruct(["F"])
    assert rover.position == (0, 2, "N")

    rover.instruct(["B", "B", "B"])
    assert rover.position == (0, -1, "N")


def test_rover_simple_path():
    rover = Rover(start_position=(1, 1, "E"))

    rover.instruct(["F", "F", "L", "B", "L", "F"])
    assert rover.position == (2, 0, "W")
