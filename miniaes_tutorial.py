"""
Disclaimer: 
    Most of the explanations, though adjusted and simplified, are taken from 
    http://staff.guilan.ac.ir/staff/users/rebrahimi/fckeditor_repo/file/mini-aes-spec.pdf
:author: Lena Heimberger
:date: 31-07-2017
"""



def start(): 
#offer to tell people about nibbles. 
    putty=input('For the following, please type yes or no. Would you like to hear about nibbles, which are the components of miniaes? ')
    if putty=='yes': 
        putty=input('A nibble\'s size is four bits. It can be thought as a finite field. Dou you know what a finite field is? ')
        if putty=='no': 
            print('A finite field is is an area of numbers where the operations +, -, * and / are all possible. If you perform them, you will stay in the field. ' + 
                    'It can be expressed as a polynomial. For example, the nibble n=1010 would be the polynomial n=1*x^3+0*x^2+1*x^1+0*x^0 ')
            putty=input('Would you like to hear more about fields?')
            if putty=='yes':
                print('Fields are a very thouroghly researched subject in maths. I would refer you the paper this program is based on. ' + 
                        'You can find it here: http://staff.guilan.ac.ir/staff/users/rebrahimi/fckeditor_repo/file/mini-aes-spec.pdf')
        print('\n')
    elif putty=='no':
        pass
    else: 
        putty=input('Sorry, I did not understand. Would you like to hear about nibbles? Type yes or no ')

#blocksize
    print('In AES, a block generally consists of 128 bits of plaintext that is turned in 128 bits of ciphertext and vice versa. '+
            'For mini-AES, we are going to use blocks of 16 bit size. \n')


#modes of operation
    putty=input('Would you like to know how the ciphertext is generated from the plaintext? ')
    if putty=='yes': 
        print('AES has so-called Modes of Operation, who determine how the ciphertext is generated from the plaintext. ' +
            'Mini-AES does not. It just encrypts block by block with the key, without taking the result of the previous block in account. This is equivalent to ' + #TODO
            'in AES. \n')

#and now start encryption
    print('Now we know a bit about the internals, how about starting to encrypt our own message with mini aes?')
    plaintext=input('Put any text you would like to encrypt here: \n')
    input('And now please press enter to continue step by step. ')
    input('\nOkay, then let\'s start. Remember the nibbles? Your text is now taken, split in 16-Bit Blocks, and in each of this block, we have now four nibbles! ' +
            'First, each nibble is rearranged in a matrix. it looks like this: \n'+
            'b0, b2 \n' +
            'b1, b3 \n' + 
            'Where b is a single bit in the nibble. \n \n')
    input('Now we can do fun stuff with the nibble matrixes. There are four operations: NibbleSub, which substitutes (replaces) a nibble with another one. \n')
    input('There is also ShiftRow, which switches the lower row of the matrix. It then looks like this: \n' + 
            'b0, b2 \n' +
            'b3, b1 \n' + 
            'instead of: \n'+ 
            'b0, b2 \n' +
            'b1, b3 \n') 


start()
