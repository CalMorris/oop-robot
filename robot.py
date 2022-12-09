from direction import Direction
from position import Position
from table_top import AbstractBoard


class Robot:
    table_top: AbstractBoard
    position: Position
    direction: Direction

    def __init__(self, table_top: AbstractBoard):
        self.table_top = table_top

    def place(self, x, y, direction):
        #Right now the robot class has a dependency on Position and Direction. We dont really want dependencies as this violates the Dependency Inversion principle in SOLID (google 'solid programming principles')
        #Have a look at what i hvae done with the table_top :)
        self.position = Position(x, y, self.table_top.get_width(), self.table_top.get_length())
        self.direction = Direction(direction)

    def turn_left(self):
        return self.direction.turn_left()

    def turn_right(self):
        return self.direction.turn_right()

    def move(self):
        return self.position.update_position(self.direction)

    def report(self):
        """
        Print the current robot position and facing direction
        """
        return print(f"Position: [ x: {self.position.get_x()}, y: {self.position.get_y()} ], Direction: {self.direction.get_direction()}")
