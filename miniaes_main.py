import argparse
from miniaes_tutorial import start
"""
This is the main class of miniaes

:author: Lena Heimberger
:date: 31.07.2017
"""

if __name__ == '__main__':
    #start with a nice welcome message
    starter=input('Welcome to the MTC3 Mini AES. If you would like a tutorial, please print \'help\'. If you are already familiar with the program, just type \'start\'\n')
    if starter=='help': 
        print('Let\'s start the tutorial on miniAES!')
        start()
    else: 
#TODO   
        print('TODO')


