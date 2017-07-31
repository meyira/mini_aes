"""
Disclaimer: 
    Most of the explanations, though adjusted and simplified, are taken from 
    http://staff.guilan.ac.ir/staff/users/rebrahimi/fckeditor_repo/file/mini-aes-spec.pdf
:author: Lena Heimberger
:date: 31-07-2017
"""



def start(): 
    #TODO
#offer to tell people about nibbles. 
    input('For the following, please type yes or no. Would you like to hear about nibbles, which are the components of miniaes?')
    label: backnibble
    if input=='yes': 
        input('A nibble\'s size is four bits. It can be thought as a finite field. Dou you know what a finite field is? ')
        if input=='no': 
            print('A finite field is is an area of numbers where the operations +, -, * and / are all possible. If you perform them, you will stay in the field.' + 
                    'It can be expressed as a polynomial. For example, the nibble n=1010 would be the polynomial n=1*x^3+0*x^2+1*x^1+0*x^0')
            input('Would you like to hear more about fields?')
            if input=='yes':
                print('Fields are a very thouroghly researched subject in maths. I would refer you the paper this program is based on. ' + 
                        'You can find it here: http://staff.guilan.ac.ir/staff/users/rebrahimi/fckeditor_repo/file/mini-aes-spec.pdf')
    elif input=='no':
        continue
    else: 
        input('Sorry, I did not understand. Would you like to hear about nibbles? Type yes or no')
        goto backnibble

start()
