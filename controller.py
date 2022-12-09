from robot import Robot

class Controller:
    def __init__(self, robot):
        self.robot = robot

    def execute(self, command, kwargs):

        if command == 'PLACE':
            #No longer passing the tabletop values to the robot becaus the robot now knows about the tabletop its sitting on.
            #This is not necessarily the best approach, just my opnion.
            return self.robot.place(**kwargs)

        if command == 'LEFT':
            return self.robot.turn_left()

        if command == 'RIGHT':
            return self.robot.turn_right()

        if command == 'MOVE':
            return self.robot.move()

        if command == 'REPORT':
            return self.robot.report()
