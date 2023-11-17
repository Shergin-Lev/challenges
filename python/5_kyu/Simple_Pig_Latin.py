"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def simplePigLatin(text: str):
    if text is None or text == '':
        return
    text = text.split(' ')
    for index, word in enumerate(text):
        if word in ['!', '?', ',', '.', '\'']:
            continue
        text[index] = word[1:] + word[0] + 'ay'
    return ' '.join(text)


print(simplePigLatin('Quis custodiet ipsos custodes ?'))
