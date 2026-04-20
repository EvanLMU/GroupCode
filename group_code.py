def string_to_numbers(string: str, mapping: dict[str:int]) -> list[int]:
    """
    Description
    The function takes a string and a mapping dictionary.
    The code returns a list in which the characters of the string have been changed to integers based on the mapping
    dictionary.
    Any character that is not found in dictionary keys is assigned the values -1.

    Input
    string: any str
    mapping: dict type in which keys are characters and the keys are integer values.

    Output
    list[int]: the string converted to numbers

    Example
    string_to_numbers(string="what's up?", mapping = {"a":1, "b":2, "c":3, etc...})
    returns: [23, 8, 1, 20, -1, 19, -1, 21, 16, -1]
    """

    # Write code here
    number_list = []

    for i in string:
        if i in mapping:

            n = mapping[i]

        else:

            n = -1

        number_list.append(n)

    return number_list


mapping = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15,
        "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}


print(string_to_numbers(string="what's up?", mapping=mapping))