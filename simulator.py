from constants import DIRECTION
from robot import Robot
import re


class Simulator(Robot):

    def __init__(self):
        self.robot = None

    def split_placement_input(self, place: str):
        return re.split("[+\s|,]", place)

    def validate_placement_input(self, placement: list):
        placement = self.split_placement_input(placement)
        assert len(placement) == 4, "Try again: you need to input the correct values to place the robot"
        assert placement[0].upper() == "PLACE", "Please try placing the robot again using the 'PLACE' command"

    def format_placement(self, placement):
        place, x, y, facing_direction = placement

        place = place.upper()
        x = int(x)
        y = int(y)
        facing_direction = facing_direction.upper()

        return [place, x, y, facing_direction]

    def handle_placement(self, place):
        INITIAL_PLACEMENT = self.split_placement_input(place)
        self.validate_placement_input(place)
        place, x, y, facing_direction = self.format_placement(INITIAL_PLACEMENT)

        return [place, x, y, facing_direction]

    def placement_command(self):
        placement = input(
            'To begin, add the following arguments seperated by a space or comma: \n \n \
                PLACE -> "PLACE": initial placement of the robot \n \
                X -> number: location (0-4) \n \
                Y -> number: location (0-4) \n \
                FACING DIRECTION: NORTH EAST SOUTH WEST \n \
                EXAMPLE: PLACE, 0, 0 NORTH \n \
        ')

        return self.handle_placement(placement)

    def start(self):
        # User input for the initial placement of the robot
        place, x, y, facing_direction = self.placement_command()
        # Set the placement of the robot
        self.set_robot(place, x, y, facing_direction)
        # Execute the commands for the robot
        self.other_commands()

    def other_commands(self):
        # Ask the user for a prompt until a request for a report
        action = self.get_action()

        while action != "REPORT":
            action = input(f'\n \
                ENTER AN ACTION:\n \
                MOVE -> MOVE THE ROBOT IN THE DIRECTION IT IS FACING (currently facing {self.get_direction()}) \n \
                LEFT -> ROTATE THE ROBOT 90 DEGREES TO THE LEFT \n \
                RIGHT -> ROTATE THE ROBOT 90 DEGREES TO THE RIGHT \n \
                REPORT -> REPORT THE CURRENT LOCATION OF THE ROBOT \n\n \
                ').upper()

            if (action == 'MOVE'):
                direction = self.get_direction()
                x, y = DIRECTION[direction]
                self.update_position(x, y)
                # self.update_position()
            if (action == 'LEFT' or action == 'RIGHT'):
                x, y =  DIRECTION[action]
                self.update_direction(action, x, y)
                return
            if (action not in ['MOVE', 'LEFT', 'RIGHT', 'REPORT']):
                print('Not a valid option')

        # Once the report is requested, the user will have an output of the location and direction that the robot is facing
        self.report_robot_position_direction()

simulator = Simulator()
simulator.start()
