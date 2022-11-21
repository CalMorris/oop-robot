from direction import Direction
from position import Position
from table_top import TableTop
from constants import DIRECTION

class Robot(TableTop, Position, Direction):
    action = 'PLACE'

    def set_robot(self, action: str, x: int, y: int, direction: str):
        assert (x <= self.width and x >= 0), f"Please enter a x value between {0} and {self.width}"
        assert (y <= self.length and y >= 0), f"Please enter a x value between {0} and {self.length}"
        assert (direction in DIRECTION), f"Please enter a valid direction -> NORTH, EAST, SOUTH or WEST"

        self.set_max_x(self.width)
        self.set_max_y(self.length)
        self.set_direction(direction)
        self.action = action

    def get_action(self):
        return self.action

    def set_action(self, action):
        self.action = action

    def report_robot_position_direction(self):
        print(f"{self.get_x()}, {self.get_y()}, {self.get_direction()}")
