import unittest

class MyTest(unittest.TestCase):
    def test1(self):
        sum_ = 2+2
        assert sum_ == 5

# if __name__ == '__main__':
#     unittest.main()