from constants import CARDINAL_VALUE

class Position():
    def __init__(self, x: str, y: str, max_x: str, max_y: str):
        self.x: int = x
        self.y: int = y
        self.max_x: int = max_x
        self.max_y: int = max_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def update_position(self, direction):

        x_diff, y_diff = CARDINAL_VALUE[direction]

        new_x = self.get_x() + x_diff
        new_y = self.get_y() + y_diff

        if self.can_update_position(new_x, self.max_x):
            self.set_x(new_x)

        if self.can_update_position(new_y, self.max_y):
            self.set_y(new_y)


    def can_update_position(self, new_value: int, max_value: int):
        """
        Check the new value is between 0 and the max_value of the table length/width.
        :param new_value: The desired value to update the position to.
        :return: Boolean -> can position be updated.
        """
        if new_value >= 0 and new_value <= max_value:
            return True
        return False
