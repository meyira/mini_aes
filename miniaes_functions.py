nibble_size=4 #a nibble is four bits. to ease the calculation, it will be four elements in an array (2-dimensional)

def str_to_bitarray(string):
"""
Turning a string in a bitarray
"""
    array=bytearray()
    array.extend(string.encode())
    print(array)

#def nibble_sub(nibble): 
    #TODO

