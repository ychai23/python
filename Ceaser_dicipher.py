#
# ps3pr3.py (Problem Set 3, Problem 3)        
#
# Caesar cipher / decipher
#

# A template for a helper function called rot that we recommend you write
# as part of your work on the encipher function.
def rot(c, n):
    """ return a new character that has been rotated by n
        input c: any character
        input n: any non-negative integer
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    # Put the rest of your code for this function below.   
    if 'a' <= c <= 'z':
        enc = ord(c) + n
    if 'a' <= c <= 'z':          # lower-case
        enc = ord(c) + n
        if enc > ord('z'):
            enc = enc - 26
    elif 'A' <= c <= 'Z':        # upper-case
        enc = ord(c) + n
        if enc > ord('Z'):
            enc = enc - 26
    else:                        # non-alpha
        enc = ord(c)
    return chr(enc)


### Put your code for the encipher function below. ###


# A helper function that could be useful when assessing
# the "Englishness" of a phrase.
# You do *NOT* need to modify this function.
def letter_prob(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for English);
        returns 1.0 for any other character.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character   
    assert(type(c) == str and len(c) == 1)

    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0

#### Put your code for the decipher function below. ####    



def list_to_string(c):
    """ returns a string conbining all the elements in the list
        input c: any list
    """
    if c == []:
        return ''
    else:
        rest = list_to_string(c[1:])
        return str(c[0]) + rest
    
def product(n):
    """ returns the product of all the posibilties of each letter in the string
        input n: any string
    """
    if n == "":
        return 1
    else:
        rest = product(n[1:])
        return rest * letter_prob(n[0])


def encipher(s, n):
    """ returns a new string in which the letters in s have been “rotated” by n characters forward in the alphabet, wrapping around as needed. 
        input s: any arbitary string
        input n: any non-negative integer
    """
    encipher1 = [rot(x, n) for x in s]
    encipher = list_to_string(encipher1)
    return encipher



def decipher(s):
    """ returns to the best of its ability, the original English string, which will be some rotation (possibly 0) of the input string s.
        input s: any string
    """
    list1 = [encipher(s, x) for x in range(0, 26)]
    list2 = [product(list1[x]) for x in range(0, 26)]
    list3 = [[list2[x], list1[x]] for x in range(0, 26)]
    score = max(list3)
    return score[1]
    
    
    