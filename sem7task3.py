import unittest
import os


#ОСТАЛЬНЫЕ 2 ЗАДАНИЯ В ВЕТКЕ sem5


a = r'C:\Users\Acer\Desktop\taskpythyo\mr_chogich'


def CreateText(a):
    os.makedirs(a)
    with open(r'C:\Users\Acer\Desktop\taskpythyo\mr_chogich\text.txt', "w") as text:
        text.write('The cake is a lie')

class TestSetUpText(unittest.TestCase):
    def setUp(self):
        self.create = CreateText(a)

    def test_assert_is_not_none(self):
        self.assertIsNotNone(r'C:\Users\Acer\Desktop\taskpythyo\mr_chogich\text.txt')
    def tearDown(self):
        os.remove(r'C:\Users\Acer\Desktop\taskpythyo\mr_chogich\text.txt')
        os.rmdir(r'C:\Users\Acer\Desktop\taskpythyo\mr_chogich')

if __name__ == 'main':
    unittest.main()
