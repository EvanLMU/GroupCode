import unittest

from group_code import string_to_numbers


class GroupCodeTestCase(unittest.TestCase):
    def test_string_to_numbers_converts_known_chars(self):
        mapping = {"a": 1, "b": 2, "c": 3}
        self.assertEqual(string_to_numbers("abc", mapping), [1, 2, 3])

    def test_string_to_numbers_maps_unknown_chars_to_minus_one(self):
        mapping = {"a": 1, "b": 2}
        self.assertEqual(string_to_numbers("ab?", mapping), [1, 2, -1])


if __name__ == "__main__":
    unittest.main()
