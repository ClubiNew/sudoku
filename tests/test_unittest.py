import unittest


class ComparisonTests(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(1, 1)

    def test_not_equal(self):
        self.assertNotEqual(0, 1)
        self.assertNotEqual(1, 0)

    def test_truthiness(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_none(self):
        self.assertIsNone(None)
        self.assertIsNotNone(True)


if __name__ == "__main__":
    unittest.main()
