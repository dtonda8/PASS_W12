import unittest
from Q1 import findKthLargest
from ed_utils.decorators import number
from tests.conversions import toBST

class Test_Q1(unittest.TestCase):
    @number("1.1")
    def test_examples(self):
        self.assertEqual(findKthLargest([3,2,1,5,6,4], 2), 5)
        self.assertEqual(findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)

    @number("1.2")
    def test_extra(self):
        self.assertEqual(findKthLargest([3,2,1,5,6,4], 3), 4)


if __name__ == '__main__':
    unittest.main()