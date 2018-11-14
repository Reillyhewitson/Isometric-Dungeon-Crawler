#ACAS Alphabet Characters and Strings

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
't', 'u', 'v', 'w', 'x', 'y', 'x']

characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '¬', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '|', '.',
 '\\', '/', '?', '<', '<', ',', ':', '@', ';', '{', '}', '[', ']', '#', '~']

def ranLowLet(): #random lower case letter
    import random
    letter = random.randint(1,26)
    letter -= 1
    return alphabet[letter]

def ranUppLet(): #random upper case letter
    import random
    letter = random.randint(1,25)
    return (alphabet[letter]).upper()

def ranMixLet(): #random upper or lower case letter
    import random
    letter = random.randint(1,25)
    case = random.randint(0,1)
    if case == 1:
        return (alphabet[letter]).upper()
    else:
        return alphabet[letter]

def letCng(letter, value): #changes the letter
    if len(letter) > 1:
        return ("Too many letters u pleb!")
    if letter[0].isupper() == True:
        case = "upper"
    else:
        case = "lower"
    letter = (letter).lower()
    number = alphabet.index(letter)
    number += value
    if number > 25:
        number = 25
    elif number < 0:
        number = 0
    if case == "upper":
        return (alphabet[number]).upper()
    elif case == "lower":
        return alphabet[number]

def ranStr(low, high): #random string
    import random
    repeat = random.randint(low, high)
    string = ""
    for dontcare in range(repeat):
        string += alphabet[random.randint(0,25)]
    return string

def wordsInSen(sentance): #splits each word in a sentance into seperate parts of a list
    sentance += " "
    word = ""
    word_list = []
    for letter in sentance:
        if letter == " ":
            word_list.append(word)
            word = ""
        else:
            word += letter
    return word_list

def ranChar(): #random charcter or letter
    import random
    letorchar = random.randint(0,66)
    if letorchar <= 26:
        return ranMixLet()
    elif letorchar <= 66:
        character = random.randint(0,40)
        return characters[character]

def split(word, quartile, half): #splits a word into the first half or the last half by either the higher quartile or the lower quartile
    if quartile == "lower":
        size = len(word) // 2
    elif quartile == "higher":
        size = len(word) // 2 + 1
    else:
        return "It should be 'split(word[sentance], quartile['lower' or 'higher'], half['first' or 'last'])'"
    if half == "first":
        return word[:size]
    elif half == "last":
        return word [size:]
    else:
        return "It should be 'split(word[sentance], quartile['lower' or 'higher'], half['first' or 'last'])'"
