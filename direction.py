class Direction():
    direction: str

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def update_direction(self, direction: str):
        """
        Rotate the direction of the robot by 90 degrees to the LEFT | RIGHT

        :param direction: The required change in direction. Example: LEFT | RIGHT
        :return: Updated direction

        TODO: Find a better implementation of changing the direction of the robot
        """
        if (direction == 'LEFT'):
            if self.get_direction() == 'NORTH':
                return self.set_direction('WEST')

            if self.get_direction() == 'EAST':
                return self.set_direction('SOUTH')

            if self.get_direction() == 'SOUTH':
                return self.set_direction('EAST')

            if self.get_direction() == 'WEST':
                return self.set_direction('NORTH')

        if (direction == 'RIGHT'):
            if self.get_direction() == 'NORTH':
                return self.set_direction('EAST')

            if self.get_direction() == 'EAST':
                return self.set_direction('SOUTH')

            if self.get_direction() == 'SOUTH':
                return self.set_direction('WEST')

            if self.get_direction() == 'WEST':
                return self.set_direction('NORTH')

