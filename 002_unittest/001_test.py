import unittest
from hamcrest import assert_that, equal_to

class MyTest(unittest.TestCase):
    def test1(self):
        sum_ = 2+2
        assert sum_ == 4
    def test2(self):
        sum_ = 2+2
        self.assertEqual (sum_,4)
    def test3(self):
        sum_ = 2+2
        asser

# if __name__ == '__main__':
#     unittest.main()