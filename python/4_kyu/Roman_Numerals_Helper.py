"""
Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
1000 -> "M"
 400 -> "CD"
  90 -> "XC"
  40 -> "XL"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"M"       -> 1000
"CD"      -> 400
"XC"      -> 90
"XL"      -> 40
"I"       -> 1
"""


class RomanNumerals:
    ROMAN_NUM_DICT = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                      'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                      'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    @staticmethod
    def to_roman(val: int):
        result = ''
        for letters, value in RomanNumerals.ROMAN_NUM_DICT.items():
            while val >= value:
                result += letters
                val -= value
        return result

    @staticmethod
    def from_roman(roman_num: str):
        result = 0
        while roman_num:
            if len(roman_num) == 1:
                result += RomanNumerals.ROMAN_NUM_DICT[roman_num]
                return result
            if RomanNumerals.ROMAN_NUM_DICT[roman_num[0]] < RomanNumerals.ROMAN_NUM_DICT[roman_num[1]]:
                result += RomanNumerals.ROMAN_NUM_DICT[roman_num[1]] - RomanNumerals.ROMAN_NUM_DICT[roman_num[0]]
                roman_num = roman_num[2:]
            else:
                result += RomanNumerals.ROMAN_NUM_DICT[roman_num[0]]
                roman_num = roman_num[1:]
        return result


print(RomanNumerals.from_roman('MDCLXVI'))
print(RomanNumerals.to_roman(3999))
