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

    def update_position(self, direction):

        try:
            new_x, new_y = self.__can_update_position(direction)
            self.x = new_x
            self.y = new_y
        except OutOfBoundsException as e:
            print(e.message)
        

    def __can_update_position(self, direction): #double __ prefix makes this a private method. calling outside this class will raise and exception
        
        x_diff, y_diff = CARDINAL_VALUE[direction.get_direction()]

        new_x = self.x + x_diff
        new_y = self.y + y_diff

        if new_x == self.x and new_y == self.y :
            return new_x, new_y
       
        if new_x <= self.max_x and new_x >= 0 and new_y <= self.max_y and new_y >= 0:
            return new_x, new_y

        raise OutOfBoundsException()

class OutOfBoundsException(Exception):
    def __init__(self, message="Can not move to new position as out of bounds"):
        self.message = message