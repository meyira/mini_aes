"""
Here is where the magic encryption happens!
:author: Lena Heimberger
:date: 31-07-2017
"""
from miniaes_functions import *

nibble_size = 4  # a nibble is four bits


def nibble_sub(nibblestr):
    """
    This acts as an S Box in mini AES
    """
    substitute = []
    for i in range(len(nibblestr)):
        if nibblestr[i] == '0000':
            substitute.append('1110')
        elif nibblestr[i] == '0001':
            substitute.append('0100')
        elif nibblestr[i] == '0010':
            substitute.append('1101')
        elif nibblestr[i] == '0011':
            substitute.append('0001')
        elif nibblestr[i] == '0100':
            substitute.append('0010')
        elif nibblestr[i] == '0101':
            substitute.append('1111')
        elif nibblestr[i] == '0110':
            substitute.append('1011')
        elif nibblestr[i] == '0111':
            substitute.append('1000')
        elif nibblestr[i] == '1000':
            substitute.append('0011')
        elif nibblestr[i] == '1001':
            substitute.append('1010')
        elif nibblestr[i] == '1010':
            substitute.append('0110')
        elif nibblestr[i] == '1011':
            substitute.append('1100')
        elif nibblestr[i] == '1100':
            substitute.append('0101')
        elif nibblestr[i] == '1101':
            substitute.append('1001')
        elif nibblestr[i] == '1110':
            substitute.append('0000')
        elif nibblestr[i] == '1111':
            substitute.append('0111')
    return substitute


def shift_row(substring):
    """
        Implements ShiftRow
        The Third and the first bit of a nibble
        are exchanged
        arg0: substring: the already nibble_subbed
        return: the shifted string
    """
    turns = len(substring)
    i=0
    print(substring)
    print("Substring len: " + str(len(substring)) + " takes turns " + str(turns))
    print(substring[0][1])
    for i in range(len(substring)):
        tmp = substring[i][1]
        substring[i][1] = substring[i][3]
        substring[i][3] = substring[i][1]
    print(substring)
    return substring


def matrix_nibble_generator(plaintext):
    # get bits
    bitstring = string_to_binary(plaintext)
    # turn them in a matrix
    nibblestr = generate_matrix(bitstring)
    # nibble sub function
    step_1 = nibble_sub(nibblestr)
    # shift row
    step_2 = shift_row(step_1)

print(matrix_nibble_generator('This is an example of'))
# for testing
