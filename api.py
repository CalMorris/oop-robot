import re
from constants import INSTRUCTIONS
from controller import Controller
from table_top import TableTop
from robot import Robot

class API:
    def __init__(self):
        table_top = TableTop(length=4,width=4) #pass the length and width values into the constructor. 
        
        #We try to pass in the classes that are required by other classe in via the constructor. 
        #This helps us conform to Liskov Substitution Principle - 
        #we can 'substiturte' the tabletop for a different implementation that also inherits from the AbstractBoard class
        robot = Robot(table_top) 
        self.controller = Controller(robot)


    def handle_command(self, command):
        split_command = re.split("[+\s|,]", command.upper().strip())

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