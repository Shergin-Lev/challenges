"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if
 that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("

Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX",
 the "XXX" is the expected result, not the input!
"""


def dub2(word: str):
    word = word.lower()
    temp_word = word
    dub_chars = []
    single_chars = []
    while temp_word:
        if temp_word.count(temp_word[0]) > 1:
            dub_chars.append(temp_word[0])
            temp_word = temp_word.replace(temp_word[0], '')
        else:
            single_chars.append(temp_word[0])
            temp_word = temp_word.replace(temp_word[0], '')
    dub_chars = ''.join(dub_chars)
    single_chars = ''.join(single_chars)
    for index in range(len(word)):
        if word[index] in dub_chars:
            word = word[:index] + ')' + word[index + 1:]
        elif word[index] in single_chars:
            word = word[:index] + '(' + word[index + 1:]
    return word


print(dub2('S(ucce)ss'))
