import unittest
from AliceCards import locate_card

class LocateCardTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(locate_card([13, 11, 10, 7, 4, 3, 1, 0],1),6)
    def test_2(self):
        self.assertEqual(locate_card([4, 2, 1, -1],4),0)      
    def test_3(self):
        self.assertEqual(locate_card([3, -1, -9, -127],-127),3)
    def test_4(self):
        self.assertEqual(locate_card([6],6),0)
    def test_5(self):
        self.assertEqual(locate_card([9, 7, 5, 2, -9],4),-1)
    def test_6(self):
        self.assertEqual(locate_card([],7),-1)
    def test_7(self):
        self.assertEqual(locate_card([ 19, 18,14, 14, 11, 11, 8, 8, 5, 3, 3, 1],5),8)
    def test_8(self):
        self.assertEqual(locate_card([ 19, 18, 14, 11, 11, 8, 7, 7, 7, 5, 3, 3, 1],7),6)    

if __name__ == "__main__":
    unittest.main()