import unittest
from hamcrest import assert_that, equal_to

Version = 0.9


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Before all")

    @classmethod
    def tearDownClass(cls):
        print("After all")

    def setUp(self):
        print("\n - start")
    def tearDown(self):
        print("END")
    @unittest.expectedFailure
    def test1(self):
        print("test1")
        sum_ = 2+2
        assert sum_ == 4
    @unittest.skip("IPH-1374")
    def test2(self):
        print("test2")
        sum_ = 2+2
        self.assertEqual (sum_,3)
    @unittest.skipIf(Version>0.9, "not support")
    def test3(self):
        print("test3")
        sum_ = 2+2
        assert_that(sum_, equal_to(3))

# if __name__ == '__main__':
#     unittest.main()