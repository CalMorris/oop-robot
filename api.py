import re
from constants import INSTRUCTIONS
from controller import Controller

class API:
    def __init__(self):
        self.controller = Controller()


    def handle_command(self, command):
        split_command = re.split("[+\s|,]", command.upper())

        if 'PLACE' in split_command:
            command, x, y, direction = split_command
            return command, {'x': int(x), 'y': int(y), 'direction': direction}

        return command.upper(), {}


    def execute(self):
        command = input(INSTRUCTIONS['placement']).upper()

        while not bool(re.match("EXIT", command)):
            command, kwargs = self.handle_command(command)
            self.controller.execute(command, kwargs)

            command = input(INSTRUCTIONS['general']).upper()

        # Terminate the programme API
        return None

if __name__ == '__main__':
    API().execute()