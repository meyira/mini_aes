"""
Here is where the magic encryption happens!
:author: Lena Heimberger
:date: 31-07-2017
"""
from miniaes_functions import *

nibble_size = 4  # a nibble is four bits

def matrix_nibble_generator(plaintext):
    # get bits
    bitstring = string_to_binary(plaintext)
    # turn them in a matrix
    matrix = generate_matrix(bitstring)


# matrix_nibble_generator('ahsdawefawefjoawe')
# for testing
