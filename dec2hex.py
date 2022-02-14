#!/usr/bin/env python
""" Converts the (fractional) decimal input number into a hexadecimal number, and displays the
    steps used in the conversion.
"""

import argparse
from typing import Tuple
from math import modf

def create_argparser() -> None:
    """ Configures an argument parser and returns it.

    Returns
    -------
    argparse.ArgumentParser
        A configured argumentparser.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "INPUT",
            help="a decimal number (with optional fractional part) to be converted to hexadecimal",
            type=float,
            action="store"
    )

    return parser

def split_float(input_num: float) -> Tuple[int, float]:
    """ Splits the non-negative input float number into its whole number part
        and its fractional part, and returns the result as a tuple.

        The fractional part is smaller than 1.
        If the input number is smaller than 1, the whole number part is zero.

    Returns
    -------
    Tuple[int, float]
        A tuple containing the whole number part and the fractional part of the input number (in that order).
    """
    # type checks
    if not isinstance(input_num, (int, float)):
        raise TypeError("Input must be an int or float.")
    if not input_num >= 0:
        raise ValueError("Input number must be non-negative.")

    fractional_part, whole_part = modf(input_num)

    return (int(whole_part), fractional_part)

def display_input_number(input_num: float) -> None:
    """ Nicely prints a summary of the input number's composition (fractional and whole part in base 10)

    Parameters
    ----------
    input_num : float
        The floating point number for which to print a summary as a base-10 number.
    """
    parts = split_float(input_num)

    # display parts and add the base-10 subscripts
    output_string = u"({})\u2081\u2080 = ({})\u2081\u2080 + ({})\u2081\u2080".format(input_num, parts[0], parts[1])

    print(output_string)

def display_conversion_by_division(input_num: int) -> str:
    """ Prints the division by conversion process of a whole number into a hexadecimal number, in a nicely
        formatted manner.

    Parameters
    ----------
    input_num : int
        The non-negative input integer, whose conversion to print.

    Returns
    -------
    str
        A string representing the input number as a hexadecimal number.
    """
    # parameter checks
    if not isinstance(input_num, int):
        raise TypeError("Input number must be an integer.")
    if not input_num >= 0:
        raise ValueError("Input number must be non-negative.")

    output_str = str()

    # calculate and save the values that will be displayed within each row in the output
    output_values = list()
    dividend = input_num
    divisor = 16
    quotient = input_num    # this is set for loop initialization
    while quotient != 0:
        dividend = quotient
        quotient = int(dividend / divisor)
        remainder_dec = dividend % divisor
        remainder_hex = '%X' % remainder_dec
        output_values.append((dividend, divisor, quotient, remainder_dec, remainder_hex))

    # build each output line with the correct padding
    max_dividend_str_width      = len(str(output_values[0][0])) + 4
    max_quotient_str_width      = len(str(output_values[0][2])) + 4
    output_lines = list()
    for value_tuple in output_values:
        line = "({})\u2081\u2080".format(value_tuple[0]).rjust(max_dividend_str_width)
        line += " : ({})\u2081\u2080 = ".format(value_tuple[1])
        line += "({})\u2081\u2080".format(value_tuple[2]).ljust(max_quotient_str_width)
        line += "    "
        line += "R({})\u2081\u2080".format(value_tuple[3]).ljust(7)
        line += " \u2192 "
        line += "({})\u2081\u2086".format(value_tuple[4])

        output_lines.append(line)
        output_str += str(value_tuple[4])

    for line in output_lines:
        print(line)

    return output_str[::-1]

def display_conversion_by_multiplication(input_num: float) -> str:
    """ Prints the conversion by multiplication process of the fractional part of a decimal number into a
        hexadecimal number, in a nicely formatted manner. Returns the result of the conversion as a string.

    Parameters
    ----------
    input_num : float
        The non-negative input float, whose conversion to print. It must be smaller than 1.

    Returns
    -------
    str
        A string representing the input number as a hexadecimal number.
    """
    # parameter checks
    if not isinstance(input_num, float):
        raise TypeError("Input number must be a float.")
    if not (input_num >= 0 and input_num < 1):
        raise ValueError("Input number must be non-negative and smaller than 1.")

    output_str = str()

    # calculate and save the values that will be displayed within each row in the output
    output_values = list()
    multiplier = input_num
    multiplicand = 16
    fractional_part = input_num     # this is set for loop initialization
    product = multiplicand * multiplier
    while int(product) != product:
        multiplier = fractional_part
        product = multiplier * multiplicand
        whole_part      = split_float(product)[0]
        fractional_part = split_float(product)[1]
        whole_part_hex  = '%X' % whole_part
        output_values.append((multiplier, multiplicand, product, whole_part_hex))

    # build each output line with the correct padding
    max_multiplier_str_width = 0
    for value_tuple in output_values:
        current_width = len(str(output_values[0][0])) + 4
        if current_width > max_multiplier_str_width:
            max_multiplier_str_width = current_width

    max_product_str_width = 0
    for value_tuple in output_values:
        current_width = len(str(output_values[0][2])) + 4
        if current_width > max_product_str_width:
            max_product_str_width = current_width

    output_lines = list()
    for value_tuple in output_values:
        line = "({})\u2081\u2080".format(value_tuple[0]).rjust(max_multiplier_str_width)
        line += " \u00B7 ({})\u2081\u2080 = ".format(value_tuple[1])
        line += "({})\u2081\u2080".format(value_tuple[2]).ljust(max_product_str_width)
        line += " \u2192 "
        line += "({})\u2081\u2086".format(value_tuple[3])

        output_lines.append(line)
        output_str += str(value_tuple[3])


    for line in output_lines:
        print(line)

    return output_str

def display_conversion_result(input_num_dec: float, converted_whole_part_hex: str, converted_fractional_part_hex: str) -> None:
    """ Prints the entire conversion in a concise and nicely formatted manner.

    Parameters
    ----------
    input_num_dec : float
        The non-negative float which was previously converted into hexadecimal number.
    converted_whole_part_hex : str
        The whole-number-part of the previously converted number, as a hexadecimal string.
    converted_fractional_part_hex : str
        The fractional-number-part of the previously converted number, as a hexadecimal string.
    """
    # parameter checks
    if not isinstance(input_num_dec, (float, int)):
        raise TypeError("Input must be an int or float.")
    if not input_num_dec >= 0:
        raise ValueError("Input decimal must be non-negative.")
    if not isinstance(converted_whole_part_hex, str):
        raise TypeError("Converted number must be a string.")
    if not isinstance(converted_fractional_part_hex, str):
        raise TypeError("Converted number must be a string.")

    print("({})\u2081\u2080 = ({},{})\u2081\u2086".format(input_num_dec, converted_whole_part_hex, converted_fractional_part_hex))



def main() -> None:
    # define and parse cmdline arguments
    parser = create_argparser()
    args = parser.parse_args()
    input_num = args.INPUT

    # display a sumar of the input number
    display_input_number(input_num)
    print()

    # split the numbers and print each conversion
    nums_split = split_float(input_num)
    whole_part_hex_str = display_conversion_by_division(nums_split[0])
    print()
    frac_part_hex_str = display_conversion_by_multiplication(nums_split[1])
    print()
    display_conversion_result(input_num, whole_part_hex_str, frac_part_hex_str)

if __name__ == "__main__":
    main()
