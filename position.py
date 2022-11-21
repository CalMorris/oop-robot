class Position():

    x: int = 0
    y: int = 0
    max_y: int
    max_x: int

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def set_max_y(self, y):
        self.max_y = y

    def set_max_x(self, x):
        self.max_x = x

    def can_update_position(self, new_value: int, max_value: int):
        """
        Check the new value is between 0 and the max_value for the table.
        """
        if new_value >=  0 and new_value <= max_value:
            return True
        return False

    def update_position(self, x_point, y_point):
        """
        Update the x and y position if the values are within the table boundaries.
        """
        new_x = self.get_x() + x_point
        new_y = self.get_y() + y_point

        if self.can_update_position(new_x, self.max_x):
            self.x = new_x
        if self.can_update_position(new_y, self.max_y):
            self.y = new_y
