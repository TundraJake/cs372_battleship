'''
Authors:
    Jacob McKenna
    Chris Bailey
    Brandon Abbott

Created 2/10/18
'''

from ship import Ship, Directions

class Board(object):

    def __init__(self):
        self.board = []
        self.length = 9

    def get_length(self):
        return self.length

    def is_valid_direction(self, direction):
        if direction not in Directions:
            return False
        return True

    def is_valid_index(self,val):
        if (val < 0 or val > self.length):
            return False
        return True

    def is_valid_placement(self, x, y, l, d):
        if not self.is_valid_index(x):
            return False
        if not self.is_valid_index(y):
            return False
        if not self.is_valid_index(l):
            return False
        if not self.is_valid_direction(d):
            return False            

        return True

    def place_ship(self, x, y, l, d):
        if not self.is_valid_placement(x,y,l,d):
            return

        self.board.append(Ship(x, y, l, d))

    def get_number_of_ships(self):
        return len(self.board)

