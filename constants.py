INSTRUCTIONS = {
    'placement': """
        To begin, add the following arguments seperated by a space or comma: \n \n \
                Keyword: "PLACE"                -> initial placement of the robot \n \
                Keyword: X                      -> number: location (0-4) \n \
                Keyword: Y                      -> number: location (0-4) \n \
                Keyword: Cardinal direction     -> NORTH EAST SOUTH WEST \n \
                EXAMPLE: PLACE 0 0 NORTH \n \
                \n \n \
        To terminate the simulation type: EXIT \n\n \
    """,
    'general': """
        ENTER AN ACTION:\n \
            MOVE -> MOVE THE ROBOT IN THE DIRECTION IT IS FACING \n \
            LEFT -> ROTATE THE ROBOT 90 DEGREES TO THE LEFT \n \
            RIGHT -> ROTATE THE ROBOT 90 DEGREES TO THE RIGHT \n \
            REPORT -> REPORT THE CURRENT LOCATION OF THE ROBOT \n\n \
    """
}

CARDINAL_VALUE = {
    'EAST': [1, 0],
    'WEST': [-1, 0],
    'NORTH':  [0, 1],
    'SOUTH': [0, -1],
}


RIGHT_DIRECTION_MAP = {
    'NORTH': 'EAST',
    'EAST': 'SOUTH',
    'SOUTH': 'WEST',
    'WEST': 'NORTH',
}

LEFT_DIRECTION_MAP = {
    'NORTH': 'WEST',
    'EAST': 'NORTH',
    'SOUTH': 'EAST',
    'WEST': 'SOUTH',
}
