#!/usr/bin/env python

""" Practice converting hexadecimal digits into binary. """

from random import randint

def main():
    while True:
        # generate a random number
        num_dec = randint(0, 16)
        num_hex = '%X' % num_dec
        num_bin = format(num_dec, 'b')
        while (len(num_bin) != 4):
            num_bin = '0' + num_bin

        user_input = input("{} in binary is:\t".format(num_hex))
        if (user_input == num_bin):
            print("Correct!")
        else:
            print("Wrong! Right answer is: {}".format(num_bin))

if __name__ == '__main__':
    main()
