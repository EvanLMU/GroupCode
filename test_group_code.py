from group_code import string_to_numbers

def test_string_to_numbers_converts_known_chars():
    mapping = {"a": 1, "b": 2, "c": 3}
    assert(string_to_numbers("abc", mapping) == [1, 2, 3])

def test_string_to_numbers_maps_unknown_chars_to_minus_one():
    mapping = {"a": 1, "b": 2}
    assert(string_to_numbers("ab?", mapping) == [1, 2, -1])