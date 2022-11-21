from constants import DIRECTION
from robot import Robot
import re


class Simulator(Robot):

    def __init__(self):
        self.robot = None

    def split_placement_input(self, place: str) -> list:
        """
        Split the placement string by space and comma.

        :param place: String of the placement of the robot. Example: "PLACE 0 0 NORTH".
        :return: Array of seperated values.
        """
        return re.split("[+\s|,]", place)

    def validate_placement_input(self, placement: list) -> None:
        """
        Validate the number of arguments and first parameter is equal to "PLACE"

        :param placement: List of arguments passed to place the robot.
        :AssertionError: Returns an error which explains the reason for invalid input.
        """
        placement = self.split_placement_input(placement)
        assert len(placement) == 4, "Try again: you need to input the correct values to place the robot"
        assert placement[0].upper() == "PLACE", "Please try placing the robot again using the 'PLACE' command"

    def format_placement(self, placement:list) -> list:
        """
        Format the input values relating to the placement of the robot.

        :param placement: List of arguments passed to place the robot.
        :return: [place:string, x: int, y: int, facing_direction:str]
        """
        place, x, y, facing_direction = placement

        place = place.upper()
        x = int(x)
        y = int(y)
        facing_direction = facing_direction.upper()

        return [place, x, y, facing_direction]

    def handle_placement(self, place: list) -> list:
        """
        Placement handler to validate, format and place the robot.

        :param place: List of arguments passed to place the robot.
        :return: [place:string, x: int, y: int, facing_direction:str]
        """
        INITIAL_PLACEMENT = self.split_placement_input(place)
        self.validate_placement_input(place)
        place, x, y, facing_direction = self.format_placement(INITIAL_PLACEMENT)

        return [place, x, y, facing_direction]

    def placement_command(self) -> list:
        """
        Invokes input for the initial robot placement.

        :param place: List of arguments passed to place the robot.
        :return: [place:string, x: int, y: int, facing_direction:str]
        """
        placement = input(
            'To begin, add the following arguments seperated by a space or comma: \n \n \
                Keyword: "PLACE"                -> initial placement of the robot \n \
                Keyword: X                      -> number: location (0-4) \n \
                Keyword: Y                      -> number: location (0-4) \n \
                Keyword: Cardinal direction     -> NORTH EAST SOUTH WEST \n \
                EXAMPLE: PLACE 0 0 NORTH \n \
        ')

        return self.handle_placement(placement)

    def start(self) -> None:
        """
        Requests the initial input and sets the robots initial location.
        """
        # User input for the initial placement of the robot
        place, x, y, facing_direction = self.placement_command()
        # Set the placement of the robot
        self.set_robot(place, x, y, facing_direction)
        # Execute the commands for the robot
        self.other_commands()

    def move_robot(self) -> None:
        """
        Moves the robot one step towards the facing location if the move is within the boandary
        of the table top.
        """
        direction = self.get_direction()
        x, y = DIRECTION[direction]
        self.update_position(x, y)

    def action_input(self) -> str:
        return input(f'\n \
            ENTER AN ACTION:\n \
            MOVE -> MOVE THE ROBOT IN THE DIRECTION IT IS FACING (currently facing {self.get_direction()}) \n \
            LEFT -> ROTATE THE ROBOT 90 DEGREES TO THE LEFT \n \
            RIGHT -> ROTATE THE ROBOT 90 DEGREES TO THE RIGHT \n \
            REPORT -> REPORT THE CURRENT LOCATION OF THE ROBOT \n\n \
            ').upper()

    def other_commands(self) -> None:
        """
        Requests and handles input for an action from the user for the robot.
        """
        # Ask the user for a prompt until a request for a report
        action = self.get_action()

        while action != "REPORT":
            action = self.action_input()

            if (action == 'MOVE'):
                self.set_action(action)
                self.move_robot()

            if (action == 'LEFT' or action == 'RIGHT'):
                self.set_action(action)
                self.update_direction(action)

            if (action not in ['PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT']):
                print('Not a valid option')

        # Once the report is requested, the user will have an output of the location and direction that the robot is facing
        self.report_robot_position_direction()
