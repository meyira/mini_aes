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


def nibbles_to_bits(nibbles):
    binary = []
    for i in range(0, len(nibbles)):
        tmp = str(nibbles[i])
        binary.append(bin(int(tmp, 2)))
    return(binary)

def string_bitwise_xor(s1, s2): 
    '''
    performing bitwise xor of s1 and s2
    :arg0: first string
    :arg1: second string
    :return: xored bit string
    '''
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
