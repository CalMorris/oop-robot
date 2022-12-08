from table_top import TableTop
from robot import Robot

class Controller:
    def __init__(self):
        self.table_top = TableTop()
        self.robot = Robot()

    def execute(self, command, kwargs):

        if command == 'PLACE':
            return self.robot.place(
                max_x = self.table_top.get_width(),
                max_y = self.table_top.get_length(),
                **kwargs
            )

        if command == 'LEFT':
            return self.robot.turn_left()

        if command == 'RIGHT':
            return self.robot.turn_right()

        if command == 'MOVE':
            return self.robot.move()

        if command == 'REPORT':
            return self.robot.report()
