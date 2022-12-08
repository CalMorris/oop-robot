from direction import Direction
from position import Position


class Robot:
    def __init__(self):
        self.position  = Position
        self.direction = Direction

    def place(self, direction, x, y, max_x = 4, max_y = 4):
        self.position = Position(x, y, max_x, max_y)
        self.direction = Direction(direction)

    def turn_left(self):
        return self.direction.turn_left()

    def turn_right(self):
        return self.direction.turn_right()

    def move(self):
        return self.position.update_position(self.direction.get_direction())

    def report(self):
        """
        Print the current robot position and facing direction
        """
        return print(f"Position: [ x: {self.position.get_x()}, y: {self.position.get_y()} ], Direction: {self.direction.get_direction()}")
