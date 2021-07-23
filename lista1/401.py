#Palindromes
import math

mirrors_dictionary = {
    'A': 'A',
    'E': '3',
    'H': 'H',
    'I': 'I',
    'J': 'L',
    'L': 'J',
    'M': 'M',
    'O': 'O',
    'S': '2',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': '5',
    '1': '1',
    '2': 'S',
    '3': 'E',
    '5': 'Z',
    '8': '8'
}


def evaluate(word):
    palindrome = True
    mirrored = True
    size = len(word)
    for i in range(math.ceil(size/2)):
        left = word[i]
        right = word[size - i - 1]  
        if left != right:
            palindrome = False
        if right != mirrors_dictionary.get(left):
            mirrored = False
    print("{} -- ".format(word), end="")
    if mirrored and palindrome:
        print("is a mirrored palindrome.")
    if not mirrored and palindrome:
        print("is a regular palindrome.")
    if mirrored and not palindrome:
        print("is a mirrored string.")
    if not mirrored and not palindrome:
        print("is not a palindrome.")
    print("")

while True:
    try:
        val = input()
        evaluate(val)
    except EOFError:
        break