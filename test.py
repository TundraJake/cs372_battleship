'''
Authors:
    Jacob McKenna
    Chris Bailey
    Brandon Abbott

Created 2/09/18
'''

import unittest
from ship import Ship, Directions

class Tests(unittest.TestCase):

    ship = Ship(1,1,5, Directions.NORTH)

    ###############################
    ######## Test Suites ##########
    ###############################

    def test_ship_xy_length_values(self):
       self.assertEqual(self.ship.get_x(),1)
       self.assertEqual(self.ship.get_y(),1)
       self.assertEqual(self.ship.get_length(),5)
       self.assertEqual(self.ship.get_direction(), Directions.NORTH)





if __name__ == '__main__':
    unittest.main()

