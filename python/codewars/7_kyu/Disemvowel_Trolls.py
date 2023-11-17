"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""


def disemvowel(string_):
    del_str = 'euioaEUIOA'
    for char in del_str:
        string_ = string_.replace(char, '') if char in string_ else string_
    return string_
