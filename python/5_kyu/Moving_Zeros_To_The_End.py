"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def movingZerosToTheEnd(val: list):
    return [num for num in val if num > 0] + [0] * val.count(0)


print(movingZerosToTheEnd([1, 0, 0, 0, 0, 1, 2, 0, 1, 3]))
