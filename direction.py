from constants import RIGHT_DIRECTION_MAP, LEFT_DIRECTION_MAP

class Direction:
    def __init__(self, direction):
        self.direction: str = direction

    def get_direction(self):
        return self.direction

    def turn_left(self):
        self.direction = LEFT_DIRECTION_MAP[self.direction]
        return self.direction

    def turn_right(self):
        self.direction = RIGHT_DIRECTION_MAP[self.direction]
        return self.direction