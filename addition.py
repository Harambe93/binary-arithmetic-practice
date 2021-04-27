#!/usr/bin/env python

# Practice binary addition for numbers X+Y=Z
# Press [ENTER] to show solution

from random import randint

largest_number = 255

x_int = randint(0, largest_number)
x_bin = bin(x_int)
# generate string representations
if x_int >= 0:
    x_int_str = str(x_int)
    x_bin_str = bin(x_int)[2:]
else:
    x_int_str = '- ' + str(x_int)[1:]
    x_bin_str = '- ' + bin(x_int)[3:]

y_int = randint(0, largest_number)
y_bin = bin(y_int)
# generate string representations
if y_int >= 0:
    y_int_str = str(y_int)
    y_bin_str = bin(y_int)[2:]
else:
    y_int_str = '- ' + str(y_int)[1:]
    y_bin_str = '- ' + bin(y_int)[3:]

z_int = x_int + y_int
z_bin = bin(z_int)
# generate string representations
if z_int >= 0:
    z_int_str = str(z_int)
    z_bin_str = bin(z_int)[2:]
else:
    z_int_str = '- ' + str(z_int)[1:]
    z_bin_str = '- ' + bin(z_int)[3:]

max_int_char_count = max(len(x_int_str), len(y_int_str), len(z_int_str))
max_bin_char_count = max(len(x_bin_str), len(y_bin_str), len(z_bin_str))

x_int_str = x_int_str.rjust(max_int_char_count, ' ')
y_int_str = y_int_str.rjust(max_int_char_count, ' ')
z_int_str = z_int_str.rjust(max_int_char_count, ' ')

x_bin = x_bin_str.rjust(max_bin_char_count, ' ')
y_bin = y_bin_str.rjust(max_bin_char_count, ' ')
z_bin = z_bin_str.rjust(max_bin_char_count, ' ')

print( "   {}     |     {}".format(x_bin, x_int_str))
print( " + {}     |   + {}".format(y_bin, y_int_str))
print(("___" + max_bin_char_count * '_' + "____ | ____" + max_int_char_count * '_'), end='')
input()
print( "   {}     |     {}".format(z_bin, z_int_str))
