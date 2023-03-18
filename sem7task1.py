import unittest


a = 0
b = [9, 8, 1, 3, 6]
c = [9, 8, 1, 0, 3]
d = 10



class TestTrue(unittest.TestCase):

    def test_true(self):
        testValue = False
        text = 'testValue - Not True'
        self.assertTrue(testValue, text)

    def test_false(self):
        testValue2 = True
        text2 = 'testValue2 - True'
        self.assertFalse(testValue2, text2)

    def test_in(self):
        text3 = 'a is not in b'
        self.assertIn(a, b, text3)

    def test_not_in(self):
        text4 = 'a is in c'
        self.assertNotIn(a, c, text4)

    def test_greater(self):
        text5 = 'a is not greater than d'
        self.assertGreater(a, d, text5)

    def test_less(self):
        text6 = 'd is greater than a'
        self.assertLess(d, a, text6)

    def test_Count_Equal(self):
        text7 = 'c is not equal to b'
        self.assertCountEqual(c, b, text7)




if __name__ == 'main':
    unittest.main()





