from constants import RIGHT_DIRECTION_MAP, LEFT_DIRECTION_MAP

class Direction:
    def __init__(self, direction):
        self.direction: str = direction

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def turn_left(self):
        direction = self.get_direction()
        return self.set_direction(LEFT_DIRECTION_MAP[direction])

    def turn_right(self):
        direction = self.get_direction()
        return self.set_direction(RIGHT_DIRECTION_MAP[direction])