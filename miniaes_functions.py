# a nibble is four bits. to ease the calculation, it will be four elements
# in an array (2-dimensional)
nibble_size = 4


def string_to_binary(string):
    """
    arg0: the string that should be converted to a binary file
    return: the string in binary representation
    """
    binary_rep = ''.join('{0:08b}'.format(ord(x), 'b') for x in string)
    return binary_rep


def generate_matrix(binary):
    """
    arg0: bitstring
    return: the bitstring split every fourth character
    """
    matrix = [binary[i:i + nibble_size]
              for i in range(0, len(binary), nibble_size)]
    return matrix
