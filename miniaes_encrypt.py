"""
Here is where the magic encryption happens!
:author: Lena Heimberger
:date: 31-07-2017
"""


def string_to_binary(string):
    """
    arg0: the string that should be converted to a binary file
    return: the string in binary representation
    """
    binary_rep = ''.join(format(ord(x), 'b') for x in string)
    return binary_rep


def matrix_nibble_generator(plaintext):
    # get bits
    bitstring = string_to_binary(plaintext)
    # turn them in a matrix
    # TODO
