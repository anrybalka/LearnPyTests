import unittest

class MyTest(unittest.TestCase):
    def test1(self):
        sum_ = 2+2
        assert sum_ == 4

    def test2(self):
        sum_ = 2+2
        self.assertEqual (sum_,4)    

# if __name__ == '__main__':
#     unittest.main()