class Direction():

    direction: str
    # def __init__(self, direction):
    #     self.direction: str = direction

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def update_direction(self, direction):
        """
        Currently this is a very gross way of setting and updating the direction that the robot is going to face
        There is probably a better mathematical way of doing this ie. string value -> int representation or vice versa
        """
        if (direction.upper == 'LEFT'):
            if self.direction == 'NORTH':
                self.set_direction('WEST')

            if self.direction == 'EAST':
                self.set_direction('SOUTH')

            if self.direction == 'SOUTH':
                self.set_direction('EAST')

            if self.direction == 'WEST':
                self.set_direction('NORTH')

        if (direction.upper == 'RIGHT'):
            if self.direction == 'NORTH':
                self.set_direction('EAST')

            if self.direction == 'EAST':
                self.set_direction('SOUTH')

            if self.direction == 'SOUTH':
                self.set_direction('WEST')

            if self.direction == 'WEST':
                self.set_direction('NORTH')

