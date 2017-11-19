"""
Here is where the magic encryption happens!
:author: Lena Heimberger
:date: 31-07-2017
"""

nibble_len = 4  # a nibble is four bits


def string_to_binary(string):
    """
    arg0: the string that should be converted to a binary file
    return: the string in binary representation
    """
    binary_rep = ''.join(format(ord(x), 'b') for x in string)
    return binary_rep


def generate_matrix(binary):
    """
    arg0: bitstring
    return: the bitstring split every fourth character
    """
    matrix = [binary[i:i + nibble_len]
              for i in range(0, len(binary), nibble_len)]
    return matrix


def matrix_nibble_generator(plaintext):
    # get bits
    bitstring = string_to_binary(plaintext)
    # turn them in a matrix
    matrix = generate_matrix(bitstring)


# matrix_nibble_generator('ahsdawefawefjoawe')
# for testing
