from direction import Direction
from position import Position
from table_top import TableTop
from constants import DIRECTION

class Robot(TableTop, Position, Direction):
    action = 'PLACE'

    def get_action(self):
        return self.action

    def set_action(self, action: str):
        self.action = action

    def validate_set_robot_input(self, x: int, y: int, direction: str):
        """
        Validates the X, Y and direction of the robot.

        :param x: Initial X location
        :param y: Initial y location
        :param direction: Initial direction that the robot will face. Example: NORTH | EAST | SOUTH | WEST
        :return: None -> implicit
        :raises AssertionError: If value is not valid
        """

        assert (x <= self.width and x >= 0), f"Please enter a x value between {0} and {self.width}"
        assert (y <= self.length and y >= 0), f"Please enter a x value between {0} and {self.length}"
        assert (direction in DIRECTION), f"Please enter a valid direction: NORTH, EAST, SOUTH or WEST"

    def set_robot(self, action: str, x: int, y: int, direction: str):
        """
        Set the initial location of the robot.

        :param action: The initial for the robot. Example: PLACE
        :param x: Initial X location
        :param y: Initial y location
        :param direction: Initial direction that the robot will face. Example: NORTH | EAST | SOUTH | WEST
        :return: None -> implicit
        """
        self.validate_set_robot_input(x, y, direction)

        self.set_max_x(self.width)
        self.set_max_y(self.length)
        self.set_direction(direction)
        self.action = action

    def report_robot_position_direction(self):
        """
        Print the current robot position and facing direction
        """
        print(f"{self.get_x()}, {self.get_y()}, {self.get_direction()}")
