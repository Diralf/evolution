import unittest

from core.geometry.convert import *


def testHTO(self, q, r, e_x, e_y):
    o = hex_to_oddr(Hex(q, r))
    self.assertEqual(o.x, e_x)
    self.assertEqual(o.y, e_y)


class TestHexToOddr(unittest.TestCase):
    def test_1_element(self):
        testHTO(self, 0, 0, 0, 0)

    def test_2_element(self):
        testHTO(self, 2, 0, 2, 0)

    def test_3_element(self):
        testHTO(self, 1, 2, 2, 2)

    def test_4_element(self):
        testHTO(self, -1, 3, 0, 3)


def testOTH(self, x, y, e_q, e_r):
    c = oddr_to_hex(Offset(x, y))
    self.assertEqual(c.q, e_q)
    self.assertEqual(c.r, e_r)


class TestOddrToHex(unittest.TestCase):
    def test_first_element(self):
        testOTH(self, 0, 0, 0, 0)

    def test_2_element(self):
        testOTH(self, 0, 2, -1, 2)

    def test_3_element(self):
        testOTH(self, 1, 2, 0, 2)

    def test_4_element(self):
        testOTH(self, 2, 1, 2, 1)


def testLTO(self, pos, w, e_x, e_y):
    off = line_to_oddr(pos, w)
    self.assertEqual(off.x, e_x)
    self.assertEqual(off.y, e_y)


class TestLineToOddr(unittest.TestCase):
    def test_first_element(self):
        testLTO(self, 0, 4, 0, 0)

    def test_first_line(self):
        testLTO(self, 5, 8, 5, 0)

    def test_few_line(self):
        testLTO(self, 20, 8, 4, 2)

    def test_first_column(self):
        testLTO(self, 16, 8, 0, 2)

    def test_last_column(self):
        testLTO(self, 9, 10, 9, 0)


def testOTL(self, x, y, w, e_pos):
    self.assertEqual(oddr_to_line(Offset(x, y), w), e_pos)


class TestOddrToLine(unittest.TestCase):
    def test_first_element(self):
        testOTL(self, 0, 0, 3, 0)

    def test_first_line(self):
        testOTL(self, 3, 0, 8, 3)

    def test_first_column(self):
        testOTL(self, 0, 3, 8, 24)

    def test_few_line(self):
        testOTL(self, 4, 5, 10, 54)

    def test_last_column(self):
        testOTL(self, 9, 5, 10, 59)


if __name__ == '__main__':
    unittest.main()
