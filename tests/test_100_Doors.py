import unittest
from 100Doors.100doors import getFinalOpenedDoors


class Test100Doors(unittest.TestCase):
    def test_100_doors(self):
        self.assertEqual(getFinalOpenedDoors(100), [])

    def test_10_doors(self):
        self.assertEqual(getFinalOpenedDoors(10), [])
    
    def test_1000_doors(self):
        self.assertEqual(getFinalOpenedDoors(1000), [])
    
    def test_0_doors(self):
        self.assertEqual(getFinalOpenedDoors(0), [])