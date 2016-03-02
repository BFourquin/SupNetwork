

class Cell(object):
    """Define a Cell, its x/y pos, type and rotation"""
    ''' Cells can be of 7 different types
     'R' router             'C' computer
     'I' straight cable     'L' angled cable
     'T' 3-end cable        'X' 4-end cable
     'O' empty cell         '''

    connections = []

    # Cell constructor
    def __init__(self, type, x, y, rotation=0):

        self.__x = x
        self.__y = y
        self.rotation = rotation
        if type in ('R', 'C', 'I', 'L', 'T', 'X', 'O'):
            self.type = type
        else:
            raise ValueError("Cell type " + type + " is wrong, check level_map in init module")
        self.set_connections()

    # Add 90° to the rotation
    def turn(self):
        self.rotation = (self.rotation + 90) % 360
        self.set_connections()

    # Actualize the list of connected cells
    def set_connections(self):
        self.connections.clear()

        if self.type == 'X' \
                or ((self.type == 'R' or self.type == 'C') and self.rotation == 0)\
                or (self.type == 'I' and (self.rotation == 0 or self.rotation == 180))\
                or (self.type == 'L' and (self.rotation == 90 or self.rotation == 180))\
                or (self.type == 'T' and self.rotation != 180):
            self.connections.append([self.__x, self.__y+1])

        if self.type == 'X' \
                or ((self.type == 'R' or self.type == 'C') and self.rotation == 90)\
                or (self.type == 'I' and(self.rotation == 90 or self.rotation == 270))\
                or (self.type == 'L' and(self.rotation == 180 or self.rotation == 270))\
                or (self.type == 'T' and self.rotation != 270):
            self.connections.append([self.__x-1, self.__y])

        if self.type == 'X'\
                or ((self.type == 'R' or self.type == 'C') and self.rotation == 180)\
                or (self.type == 'I' and (self.rotation == 0 or self.rotation == 180))\
                or (self.type == 'L' and (self.rotation == 270 or self.rotation == 0))\
                or (self.type == 'T' and self.rotation != 0):
            self.connections.append([self.__x, self.__y-1])

        if self.type == 'X'\
                or ((self.type == 'R' or self.type == 'C') and self.rotation == 270)\
                or (self.type == 'I' and (self.rotation == 90 or self.rotation == 270))\
                or (self.type == 'L' and (self.rotation == 0 or self.rotation == 90))\
                or (self.type == 'T' and self.rotation != 90):
            self.connections.append([self.__x+1, self.__y])

        print(self.connections)
