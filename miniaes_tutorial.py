"""
Disclaimer:
    Most of the explanations, though adjusted and simplified, are taken from
    http://staff.guilan.ac.ir/staff/users/rebrahimi/fckeditor_repo/file/mini-aes-spec.pdf
:author: Lena Heimberger
:date: 2017-07-31
"""
import random
import string


def nibble():
    """
    Pressuring the user to clearly state if they want to know about nibbles.
    This is only done once, as afterwards, only a clear yes results in more
    information.
    """
    putty = input(
        'Sorry, I did not understand. Would you like to hear about ' +
        'nibbles? ' +
        'Type yes or no ')
    if putty == 'yes':
        putty = input(
            'A nibble\'s size is four bits. ' +
            'It can be thought as a finite field. ' +
            'Dou you know what a finite field is? ')
    elif putty == 'no':
        return
    else:
        nibble()


def start():
    # offer to tell people about nibbles.
    putty = input(
        'For the following, please type yes or no. ' +
        'Would you like to hear about details(nibbles), ' +
        'which are the components of mini-AES? ')
    if putty == 'yes':
        putty = input(
            'A nibble\'s size is four bits. ' +
            'It can be thought as a finite field. ' +
            'Dou you know what a finite field is? ')
        if putty == 'no':
            print(
                'A finite field is is an area of numbers where the ' +
                'operations +, -, * and / are all possible. ' +
                'If you perform them, you will stay in the field. ' +
                'It can be expressed as a polynomial. For example, ' +
                'the nibble n=1010 would be the polynomial ' +
                'n=1*x^3+0*x^2+1*x^1+0*x^0 ')
            putty = input('Would you like to hear more about fields?')
            if putty == 'yes':
                print(
                    'Explaining fields so everybody understands them ' +
                    'exceeds this program\'s scope. For further reference, ' +
                    'please refer you the paper this program is based on. ' +
                    'You can find it here: ' +
                    'http://staff.guilan.ac.ir/staff/users/rebrahimi/' +
                    'fckeditor_repo/file/mini-aes-spec.pdf')
        print('\n')
    elif putty == 'no':
        pass
    else:
        nibble()

# blocksize
    print(
        'In AES, a block generally consists of 128 bits of plaintext that is' +
        ' turned in 128 bits of ciphertext and vice versa. ' +
        'For mini-AES, we are going to use blocks of 16 bit size.\n')


# modes of operation
    putty = input(
        'Would you like to know how the ciphertext is ' +
        'generated from the plaintext? ')
    if putty == 'yes':
        print('AES has so-called Modes of Operation, who determine how' +
              'the ciphertext is generated from the plaintext. ' +
              'Mini-AES does not. It just encrypts block by block with the' +
              'key, without taking the result of the previous block in ' +
              'account. This is equivalent to the insecure electronic ' +
              'codebook mode in AES. It should not be used in real programs.')

# and now start encryption
# starting here, input() is used, so the user can read in their own time
# they are instructed to press enter as soon as they have finished reading
# a section
    print('Now we know a bit about the internal functions, ' +
          'how about starting to encrypt our own message with mini-AES?')
    plaintext = input('Enter the text you would like to encrypt here:\n')
    input('And now please press enter to continue step by step. ')
    input(
        '\nOkay, then let\'s start. Remember the nibbles? ' +
        'Your text is taken, split in 16-Bit Blocks, and ' +
        'in each block, we have four nibbles, each consiting of four bits.' +
        'First, each nibble is rearranged in a matrix. It looks like this: ' +
        '\nb0, b2 \n' +
        'b1, b3 \n' +
        'Where b is a single bit in the nibble.\n\n')

# explanation of the four main components

# NibbleSub explanation
    input('Now we can do fun stuff with the nibble matrixes. ' +
          'There are four operations: NibbleSub, which substitutes ' +
          '(replaces) a nibble with another one.\n')
# ShiftRow explanation
    input(
        'There is also ShiftRow, which switches the lower row of the matrix.' +
        ' It then looks like this:\n' +
        'b0, b2\n' +
        'b3, b1\n' +
        'instead of:\n' +
        'b0, b2\n' +
        'b1, b3\n')
# MixColumn explanation
    input('In MixColumn, each column of the input block is multiplied ' +
          'with a constant matrix to get a new column. If you do not ' +
          'understand matrix multiplication, you should read into it ' +
          'before you continue. \n')
# Key Use
    key = input(
        'To make sure only authorized persons can access and decrypt the ' +
        'files, a key is created that can be shared with trusted persons.\n' +
        'For demonstration purposes, you may now create your own key:\n')
    if len(key) == 1:
        key = input(
            'The key needs to have at least two letters. Please enter two.')
    if len(key) == 1:
        key = input(
            'The key needs to be longer. I will now create one for you: ')
        for i in range(16):
            key += random.choice(string.ascii_uppercase +
                                 string.ascii_lowercase + string.digits)
            print(str(key) + '\n')
    if not key:
        print('You did not enter a key. To continue, I created one for you: ')
        for i in range(16):
            key += random.choice(string.ascii_uppercase +
                                 string.ascii_lowercase + string.digits)
        print(str(key) + '\n')
        input(
            'Remember, this program is entirely educational! The resulting ' +
            'ciphertext is easy to break and should not be used ' +
            'to encrypt sensitive data!')

# KeyAddition
    input('We are now going to use the key for the last ' +
          'operation, the KeyAddition. For this, the block is XORed (' +
          'exclusive OR) with the key.\n')

# Mini AES Key schedule/key derivation
    input('Now, there are three keys generated from the original key. ' +
          'They are going to be called K0, K1 and K2, and are used ' +
          'in each round of encrypting the text. A round is a pass '
          'of plaintext through the encryption proceidure. AES uses '
          '10 to 14, depending on the key size.\n')
# key derivation of K0
    input('For the first round of key derivation, the output key, K0, ' +
          'is just going to be our original key, both 16 bits long. ' +
          'If our key is longer, it does not matter, as only the first ' +
          '16 bits are going to be used. ')
    input('K0 is used before the first round. The plaintext is now put ' +
          'through the operations we got to know, which ' +
          'are used in following order: \n' +
          'NibbleSub, ShiftRow, MixColumn, KeyAddition, where the ' +
          'key is XORed with the intermediate result, another NibbleSub ' +
          'and another ShiftRow, resulting in the first block of plaintext: ')
    print('              ___        ___        _____        ____ \n' +
          '             |   |      |  /|      | ^ ^ |      |\\  /|\n' +
          'Plaintext--->| S |----->| / |----->| | | |----->| \\/ |\n' +
          '             |___|      |/__|      |_|_|_|      |_/\\_|\n\n' +
          '            NibbleSub  ShiftRow    MixColumn    KeyAddition \n' +
          '                                                   |   \n' +
          '               ____________________________________|   \n' +
          '              |                                        \n' +
          '             \ /\n' +
          '              ___        ___        _____ \n' +
          '             |   |      |  /|      |ccccc|\n' +
          '             | S |----->| / |----->|ccccc|\n' +
          '             |___|      |/__|      |ccccc|\n\n' +
          '            NibbleSub  ShiftRow    Ciphertext \n')
