import unittest


class TestSubTest(unittest.TestCase):
    def test_sub_test(self):
        a = 10
        text = 'i is not greater than a'
        for i in range(5, 15):
            with self.subTest(i=i):
                self.assertGreater(i, a, text)


if __name__ == 'main':
    unittest.main()


