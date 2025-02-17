import unittest

from main import do_foo


class TestFoo(unittest.TestCase):
    def test_do_foo(self):
        res = do_foo(1, 2)
        self.assertEqual(res, 6)

        res = do_foo(0, 0)
        self.assertEqual(res, 0)
